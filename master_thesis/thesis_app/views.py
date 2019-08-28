from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from .forms import step_1Form, step_2Form,countriesFormset,UsabilitySurveyForm
from .choices import *
from .models import user_rate,country_name,step_1,step_2,usabilitySurvey,user_result
from django.forms import formset_factory
from django import forms
from sre_compile import _compile_info
from .app import *


query = country_name.objects.all()


#------------------------------- Personal Information -------------------
def personal_info(request):
    auth_user = request.user
    if request.user.is_authenticated:
        auth_user = request.user
        if(step_1.objects.filter(user_id=auth_user).delete()):
            print('')
        if request.method == "POST":
            form = step_1Form(request.POST or None)
            if form.is_valid():
                answer1  = form.save(commit = False)
                answer1.user_id = request.user  
                answer1.save()
                return redirect('thesis_app:features')

    else :
        return redirect('thesis_app:login')
    user = request.user
    form  = step_1Form(request.POST or None)
    return render(request, 'thesis_app/personal_info.html',context={'user':user,'form':form})


#------------------------------- Features --------------------------------
def features(request):
    auth_user = request.user
    if request.user.is_authenticated :
        auth_user = request.user
        # test if user take the firsts steps
        if(step_1.objects.filter(user_id=auth_user)):
            print('Exist')
        else :
            return redirect('thesis_app:personal_info')
        
        # if user comeback to change their choices
        if(step_2.objects.filter(user_id=auth_user).delete()):
            print('')
        if request.method == 'POST':
            form = step_2Form(request.POST or None)
            if form.is_valid():
                answer2 =form.save(commit = False)
                answer2.user_id = request.user
                answer2.save()
                return redirect('thesis_app:countries_rate')
    else:
        return redirect('thesis_app:login')  
    user = request.user
    form = step_2Form(request.POST or None)        
    return render(request,'thesis_app/features.html',context = {'user':user,'form':form})
    

#------------------------------- Countries Rate --------------------------

def countries_rate(request): 
    auth_user = request.user
    if request.user.is_authenticated:
        auth_user = request.user
        
        # test if user take the firsts steps
        if(step_1.objects.filter(user_id=auth_user)):
            print('Exist')
        else :
            return redirect('thesis_app:personal_info')
        
        # if user comeback to change their choices
        if(user_rate.objects.filter(user_id=auth_user).delete()):
            print('')
        formset = countriesFormset(request.POST or None)
        if request.method == 'POST':
            if 'Add_More' in request.POST:
                #print('--- add more in post -----')
                cp = request.POST.copy()
                cp['form-TOTAL_FORMS'] = int(cp['form-TOTAL_FORMS'])+ 1
                formset = countriesFormset(cp,prefix='form')
                total = cp['form-TOTAL_FORMS']
                #print('total forms {}---------------------',format(total))
                return render(request,'thesis_app/countries_rate.html', context={
        'formset':formset,
        'total':total
        })
            elif 'submit' in request.POST:
                if formset.is_valid():
                    for inst in formset:
                        rate  = user_rate()
                        if inst.is_valid():
                            #answer2 =inst.save(commit = False)
                            #answer2.user_id = auth_user
                            countries_name_id  = inst.cleaned_data.get('countries_name_id')
                            country_rating = inst.cleaned_data.get('country_rating')
                            rate.user_id = auth_user
                            rate.countries_name_id = countries_name_id
                            rate.country_rating = country_rating
                            #print(auth_user,"................")
                            rate.save()
                            
                    return redirect('thesis_app:result')
        
    else:
        return redirect('thesis_app:login')            
    user = request.user
    formset = countriesFormset(request.POST or None)
    return render(request,'thesis_app/countries_rate.html', context={
        'user':user,
        'formset':formset
        }
    )
        
#------------------------------- Result --------------------------

def result(request):
    if request.user.is_authenticated:
        auth_user = request.user
        
        #add rating of curent user to the csv file
        target_user_id = add_to_csv(auth_user)
        
        # compute the recomendation
        recom_alg = 'other'
        recom_size = 9

        top_n_for_target_user = get_top_n_for_user(target_user_id, recom_alg, recom_size)
        print(top_n_for_target_user)
        
        # get country name
        recommendations = []
        for i in range(len(top_n_for_target_user)):
            recommendations.append(top_n_for_target_user[i][0])
        
        recommended_countries = []
        
        for C_id in recommendations:
            recommended_countries.append(list(country_name.objects.filter(id = C_id).values_list('country_name', flat = True))) 
       
        if(step_1.objects.filter(user_id=auth_user)):
            print('')
        else :
            return redirect('thesis_app:personal_info')
        if request.method == 'POST':
            if 'submit' in request.POST:
                return redirect('thesis_app:UsabilitySurvey')
    else:
        return redirect('thesis_app:login')   
    
    # save result to database
    for r in recommended_countries:
        user_recomded = user_result()
        user_recomded.user_id =  auth_user
        user_recomded.countries_name = str(r[0])
        if recom_alg == 'KNNBaseline_user' or recom_alg == 'KNNBaseline':
            user_recomded.algorithm = recom_alg
        else:
            user_recomded.algorithm = 'SVD'
        user_recomded.save()
   
    rated_1_3 =[]  
    rated_3_6 =[] 
    rated_6_9 =[] 

    for i in recommended_countries[:3]:
        rated_1_3.append(i[0])
       
        
    for i in recommended_countries[3:6]:
        rated_3_6.append(i[0])
        
    for i in recommended_countries[6:9]:
        rated_6_9.append(i[0])
        
    # rated_1_3 = recommended_countries[:3]
    # rated_3_6 = recommended_countries[3:6]
    # rated_6_9 = recommended_countries[6:9]

    print('--------->',rated_1_3,rated_3_6, rated_6_9)
    args = {"Fst_3":rated_1_3,"Snd_3":rated_3_6, "Trd_3":rated_6_9,"user":auth_user}   
    return render(request, 'thesis_app/result.html', args)








#------------------------ Usability Survey -----------------------
def UsabilitySurvey(request):
    auth_user = request.user
    if request.user.is_authenticated :
        auth_user = request.user
        if(step_1.objects.filter(user_id=auth_user)):
            print('Exist')
        else :
            return redirect('thesis_app:personal_info')
        if (usabilitySurvey.objects.filter(user_id=auth_user).delete()):
            print('')
        if request.method == 'POST':
            form = UsabilitySurveyForm(request.POST or None)
            if form.is_valid():
                answer2 = form.save(commit = False)
                answer2.user_id = request.user
                answer2.save()
                return redirect('thesis_app:thanks')
    else:
        return redirect('thesis_app:login')
    user = request.user
    form = UsabilitySurveyForm(request.POST or None)        
    return render(request,'thesis_app/UsabilitySurvey.html',context = {'user':user,'form':form})

#------------------------------- thanks --------------------------

def thanks(request):
    return render(request, 'thesis_app/thanks.html', context={})
#-------------------------------- how works ----------------------
def howWorks(request):
    return render(request,'thesis_app/howWorks.html', context={})













#------------------------------- home  -------------------------
def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            new_user  = form.save(commit = False)
            new_user.user_id = request.user  
            new_user.save()
            login(request, new_user)
            base_url = 'thesis_app:personal_info'
            #Chosen_url = form.cleaned_data['username']
            return redirect(base_url)
            

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "thesis_app/home.html",
                          context={"form":form})

    form = RegistrationForm
    return render(request = request,
                  template_name = "thesis_app/home.html",
                  context={"form":form})

#------------------------------- logout -------------------------
def logout_request(request):
    logout(request)
    return redirect('thesis_app:home')

#------------------------------- login --------------------------
def login_request(request):
    if request.user.is_authenticated:
        return redirect('thesis_app:home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request,data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password  = form.cleaned_data.get('password')
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('thesis_app:redirect_login')
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'Invalid username or password')   
        form  = AuthenticationForm()
        return render(request, 'thesis_app/login.html',{'form':form})



# -------------------- redirect login -----------------        
def redirect_login(request):
    if request.user.is_authenticated:
        result = []
        result  = list(user_result.objects.filter(user_id=request.user).values_list('countries_name',flat = True))
        
        rated_1_3 = result[:3]
        rated_3_6 = result[3:6]
        rated_6_9 = result[6:9]
        
        
        if len(result) == 0:
            nr = 'Sorry'
            return render(request, 'thesis_app/user_login.html', context={'result':nr})
        else :
            return render(request, 'thesis_app/user_login.html', context={'r1':rated_1_3,'r2':rated_3_6,'r3':rated_6_9})
            
    
    
    
    
    
    
def error_404(request,exception):
    data = {}
    return render(request, 'thesis_app/404.html',data)
def error_500(request):
        data = {}
        return render(request,'thesis_app/404.html', data)