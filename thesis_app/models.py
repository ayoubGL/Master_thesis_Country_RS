from django.db import models
from django.utils import timezone
from django.conf import settings
from django_countries.fields import CountryField
from django_countries import countries 


  
class step_1(models.Model):
    
    # ________________gender__________________
    Male ='Male'
    Female ='Female'
    refuse_to_disc = 'Refuse to disclose'
    # ________________Age__________________
    under_18 = 'under_18'
    b18_24 = '18_24'
    b25_35 = '25_35'
    b35_45 = '35_45'
    b45_55 = '45_55'
    bover_55 = 'Over_55'
    # ______________ choices  Level ___________
    Strongly_Disagree  ='Strongly Disagree'
    Disagree = 'Disagree'
    Neutral = 'Neutral'
    Agree = 'Agree'
    Strongly_Agree='Strongly Agree'
    
    
    Gender_choices = [
        (Male,'Male'),
        (Female,'Female'),
        (refuse_to_disc,'Refuse to disclose')
    ]
    
    Age_choices = [
        (under_18,'under_18'),
        (b18_24,'18_24'),
        (b25_35,'25_35'),
        (b35_45,'35_45'),
        (b45_55,'45_55'),
        (bover_55,'Over_55')
    ]
    Imaginative_choices =[
        (Strongly_Disagree,'Strongly Disagree'),
        (Disagree,'Disagree'),
        (Neutral,'Neutral'),
        (Agree,'Agree'),
        (Strongly_Agree,'Strongly Agree')
    ]
    Organized_choices =[
        (Strongly_Disagree,'Strongly Disagree'),
        (Disagree,'Disagree'),
        (Neutral,'Neutral'),
        (Agree,'Agree'),
        (Strongly_Agree,'Strongly Agree')
    ]
    Enthusiastic_choices =[
        (Strongly_Disagree,'Strongly Disagree'),
        (Disagree,'Disagree'),
        (Neutral,'Neutral'),
        (Agree,'Agree'),
        (Strongly_Agree,'Strongly Agree')
    ]
    kind_choices =[
        (Strongly_Disagree,'Strongly Disagree'),
        (Disagree,'Disagree'),
        (Neutral,'Neutral'),
        (Agree,'Agree'),
        (Strongly_Agree,'Strongly Agree')
    ]
    Calm_choices =[
        (Strongly_Disagree,'Strongly Disagree'),
        (Disagree,'Disagree'),
        (Neutral,'Neutral'),
        (Agree,'Agree'),
        (Strongly_Agree,'Strongly Agree')
    ]
    
    title = models.CharField(
        max_length = 20, 
        editable=False,
        default = 'step1'
    )
    
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    gender = models.CharField(
        choices = Gender_choices,
        max_length = 20,
        verbose_name = 'gender',
        default = Gender_choices[0][0]
    )
    
    age = models.CharField(
        choices = Age_choices,
        max_length = 40,
        verbose_name = 'age',
        default = Age_choices[0][0]
    )
    
    country = CountryField(multiple = False,default= dict(countries)['NZ'])
    
    imaginative = models.CharField(
        choices = Imaginative_choices,
        max_length = 20,
        verbose_name = 'imaginative',
        default = Imaginative_choices[0][0]
    )
    organized = models.CharField(
        choices = Organized_choices,
        max_length = 20,
        verbose_name = 'organized',
        default = Organized_choices[0][0]
    )
    enthusiastic  = models.CharField(
        choices = Enthusiastic_choices,
        max_length = 20,
        verbose_name = 'enthusiastic',
        default = Enthusiastic_choices[0][0]
    )
    kind = models.CharField(
        choices = kind_choices,
        max_length = 20,
        verbose_name = 'kind',
        default = kind_choices[0][0]
    )
    calm = models.CharField(
        choices = Calm_choices,
        max_length = 20,
        verbose_name = 'calm',
        default = Calm_choices[0][0]
    )
    
    class Meta:
        verbose_name= 'step_1'
        ordering = ['user_id']
    def __str__(self):
        return self.title
        
        
# Create your models here.




# TITLE_CHOICES = [
#     ('MR', 'Mr.'),
#     ('MRS', 'Mrs.'),
#     ('MS', 'Ms.'),
# ]

# class Author_2(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=3, choices=TITLE_CHOICES,default =TITLE_CHOICES[0][0])
#     birth_date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return self.name