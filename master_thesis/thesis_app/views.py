from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from .forms import step_1Form, step_2Form,user_rateForm,country_nameFrom,user_rateForm
from .choices import *
import pandas as pd
import csv
from .models import user_rate
from django.forms import formset_factory



#------------------------------- Personal Information -------------------
def personal_info(request):
    if request.user.is_authenticated:
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
    if request.user.is_authenticated :
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
    if request.user.is_authenticated:
        countriesFormset = formset_factory(user_rateForm, extra = 2,max_num=1)
        if request.method == 'POST':
            #form = user_rateForm(request.POST or None)
            form  = countriesFormset(request.POST)
            #print(form.errors,'---------------- errors---------')
            if form.is_valid():
                print("---------------------------------------------->{}".format(len(form)))
                for inst in form:
                    rate  = user_rate()
                    if inst.is_valid():
                        countries_name_id  = inst.cleaned_data['countries_name_id']
                        country_rating = inst.cleaned_data['country_rating']
                        rate.user_id = request.user
                        rate.countries_name_id = countries_name_id
                        rate.country_rating = country_rating
                        rate.save()
                return HttpResponse("your are here")
    else:
        return redirect('theisis_app:login')            
    user = request.user
    form = formset_factory(user_rateForm, extra =2)
    return render(request,'thesis_app/countries_rate.html', context={
        'user':user,
        'form':form,
        }
    )

# def rate_countries(request):
#     if request.user_is_authenticated:
        
    
        
        
        
        
        
        # user = request.user
        # my_csv = pd.read_csv("static/new_countries.csv")
        # head_csv = my_csv.head()
        # for step in step_2.objects.all():
        #     if step.user_id == user:
        #         features_user = step.features 
        #         print(list(features_user))
        # return render(request,'thesis_app/countries_rate.html', context={'user':request.user,'features':features_user, 'csv':head_csv})














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
            return redirect('thesis_app:personal_info')

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
        # return redirect(request,'thesis_app/survey_page.html',context={'user':request.user})
        return redirect('thesis_app:survey_page')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request,data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password  = form.cleaned_data.get('password')
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('thesis_app:survey_page')
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'Invalid username or password')   
        form  = AuthenticationForm()
        return render(request, 'thesis_app/login.html',{'form':form})
        
    