from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from .forms import step_1Form
from .choices import *



def survey_page(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = step_1Form(request.POST or None,initial={
                'gender':Gender_choices[0][0],
                'age': Age_choices[0][0],
                'country': 'GB',
                'imaginative':Imaginative_choices[0][0],
                'organized':Organized_choices[0][0],
                'enthusiastic':Enthusiastic_choices[0][0],
                'kind':kind_choices[0][0],
                'calm':Calm_choices[0][0],
            })
            answer1  = form.save(commit = False)
            answer1.user_id = request.user  
            answer1.save()
            return redirect('thesis_app:survey_page_2')
    else :
        return redirect('thesis_app:login')
    user = request.user
    form  = step_1Form(request.POST or None,initial={
                'gender':Gender_choices[0][0],
                'age': Age_choices[0][0],
                'imaginative':Imaginative_choices[0][0],
                'organized':Organized_choices[0][0],
                'enthusiastic':Enthusiastic_choices[0][0],
                'kind':kind_choices[0][0],
                'calm':Calm_choices[0][0],
            })
    return render(request, 'thesis_app/survey_page.html',context={'user':user,'form':form})

def survey_page_2(request):
    context_txt = 'Hello to the survey_2'
    return render(request,'thesis_app/survey_page_2.html',context = {'text':context_txt})






def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            new_user.save()
            login(request, new_user)
            return redirect('thesis_app:survey_page')

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



    


def logout_request(request):
    logout(request)
    return redirect('thesis_app:home')


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
        
    