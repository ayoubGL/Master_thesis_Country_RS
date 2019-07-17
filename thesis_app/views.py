from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def survey_page(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'thesis_app/survey_page.html',context={'user':user})
    else :
        return redirect('thesis_app:login')



def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("survey_page/")

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



    



# def home(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("survey_page/")

#         else:
#             for msg in form.error_messages:
#                 print(form.error_messages[msg])

#             return render(request = request,
#                           template_name = "thesis_app/home.html",
#                           context={"form":form})

#     form = UserCreationForm
#     return render(request = request,
#                   template_name = "thesis_app/home.html",
#                   context={"form":form})

def logout_request(request):
    logout(request)
    return redirect('thesis_app:home')


def login_request(request):
    if request.user.is_authenticated:
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
        
    