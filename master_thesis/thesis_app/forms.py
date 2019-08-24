from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .models import step_1, step_2,country_name,UsabilitySurvey,user_rate
from django.contrib.auth import get_user_model
from django_starfield import Stars
from django_countries.fields import CountryField
User = get_user_model()

from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Row, Field

from django.forms.formsets import BaseFormSet
from django.forms import formset_factory  









class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True) 
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    def save(self,commit = True):
        user = super(RegistrationForm,self).save(commit = False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user

        # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = "col-md-4"
    helper.field_class = "col-md-8"
    
  
  
  
        
class step_1Form(forms.ModelForm):
    class Meta:
        model = step_1
        exclude = ('titre','user_id')
        widgets = {
            'gender': forms.RadioSelect(),
            'age':forms.Select(attrs={'class' : 'select form-control col-sm-4'}),
            'country':forms.Select(attrs={'class' : 'select form-control col-sm-4'}),
            'imaginative':forms.RadioSelect(),
            'organized':forms.RadioSelect(),
            'enthusiastic':forms.RadioSelect(),
            'kind':forms.RadioSelect(),
            'calm':forms.RadioSelect(),
        }
        labels  = {
            'gender': 'Gender',
            'age':'Age',
            'Country':'Where are you from ?',
            'imaginative':'I see myself as open to experience, imaginative',
            'organized':'I see myself as dependable, organized',
            'enthusiastic':'I see myself as extraverted, enthusiastic',
            'kind':'I see myself as agreeable, kind',
            'calm':'I see myself as emotionally stable, calm',
        }
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = "col-md-4"
    helper.field_class = "col-md-8"


class step_2Form(forms.ModelForm):
    class Meta:
        model = step_2
        exclude = ('title', 'user_id')
    helper = FormHelper()
    helper.form_class = 'form-vertical'
    helper.label_class = "col-md-8"
    helper.field_class = "col-md-8"



query = country_name.objects.all()
''
class user_rateForm(forms.ModelForm):
    countries_name_id = forms.ModelChoiceField(queryset=query,required=True) 
    country_rating =  forms.IntegerField(required=True,widget=Stars())
    
    class Meta:
        model = user_rate
        exclude = ('titre','user_id')
        
    
    def __init__(self, *args, **kwargs):
        super(user_rateForm, self).__init__(*args, **kwargs)
        self.fields['countries_name_id'].label = False
        self.fields['country_rating'].label = False
        self.fields['countries_name_id'].required = True
        self.fields['country_rating'].required = True
        self.fields['country_rating'].error_messages['required'] = 'I require that you fill out this field'


                         
countriesFormset = formset_factory(user_rateForm, extra = 5,max_num=20)              

    
class UsabilitySurveyForm(forms.ModelForm):
    class Meta:
        model = UsabilitySurvey
        exclude = ('title', 'user_id')
        widgets = {     
            'usage_frequency':forms.RadioSelect(),
            'system_complexity':forms.RadioSelect(),
            'usage_ease':forms.RadioSelect(),
            'need_help':forms.RadioSelect(),
            'functions_integrated':forms.RadioSelect(),
            'system_inconsistency':forms.RadioSelect(),
            'learn_to_use':forms.RadioSelect(),
            'system_inconvenient':forms.RadioSelect(),
            'confident_level':forms.RadioSelect(),
            'learning_before':forms.RadioSelect(),
            'comment':forms.Textarea(),
            'email':forms.EmailInput(),
        }   
        labels  = {
            'comment': '',
            'email':'',
        }
        
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = "col-md-4"
    helper.field_class = "col-md-8"
