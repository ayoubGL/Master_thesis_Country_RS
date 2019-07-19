from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .models import step_1
from django.contrib.auth import get_user_model
User = get_user_model()





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

  
  
  
        
class step_1Form(forms.ModelForm):
    class Meta:
        model = step_1
        exclude = ('titre','user_id')
        widgets = {
            'gender': forms.RadioSelect(),
            'age':forms.Select(),
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
        



# TITLE_CHOICES = [
#     ('MR', 'Mr.'),
#     ('MRS', 'Mrs.'),
#     ('MS', 'Ms.'),
# ]


# class AuthorForm(forms.ModelForm):
#     title = forms.ChoiceField(label='What is your favorite title?',widget=forms.RadioSelect(), choices=TITLE_CHOICES)
#     class Meta:
#         model = Author_2
#         fields = ['name', 'birth_date', 'title']

    
        