from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from . choices import * 

from django.contrib.auth import get_user_model
User = get_user_model()





class RegistrationForm(UserCreationForm):
    Email = forms.EmailField(required = True) 
    #gender = forms.ChoiceField(required = True, label='Gender',choices = Gender_choices)
    #Age = forms.ChoiceField(required = True,label='Age',choices = Age_choices)
    # #Country = CountryField(blank_label = '(Where you live)',multiple = False)  
    
    class Meta:
        model = User 
        fields = ['username','Email','password1','password2']#``,'gender','Age']
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
    
   

    



    
        