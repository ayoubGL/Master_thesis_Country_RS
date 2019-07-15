from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm
# Create your views here.
    
def survey_page(request):
    return render(request, 'thesis_app/survey_page.html',locals())

def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
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


    

# def login(request):
#     return render(request, 'registration/login.html',locals())



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
