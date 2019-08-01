from django.db import models
from django.utils import timezone
from django.conf import settings
from django_countries.fields import CountryField
from django_countries import countries 
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import *

# ---------------------------------------------- Personal Information ------------------------
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
    #------------------------- Fields ------------------------
    title = models.CharField(
        max_length = 20, 
        editable=False,
        default = 'step1'
    )
    
    user_id = models.ForeignKey(
        User,
        default = 1,
        on_delete=models.CASCADE
        
    )
    
    gender = models.CharField(
        choices = Gender_choices,
        max_length = 20,
        verbose_name = 'gender',
        default=None,
        blank=False
   
    )
    
    age = models.CharField(
        choices = Age_choices,
        max_length = 40,
        verbose_name = 'age',
        default=None,
        blank=False
    )
    
    country = CountryField(multiple = False,
                           default=None,
                            blank=False)
    
    imaginative = models.CharField(
        choices = Imaginative_choices,
        max_length = 20,
        verbose_name = 'imaginative',
        default=None,
        blank=False
       
    )
    organized = models.CharField(
        choices = Organized_choices,
        max_length = 20,
        verbose_name = 'organized',
        default=None,
        blank=False
       
    )
    enthusiastic  = models.CharField(
        choices = Enthusiastic_choices,
        max_length = 20,
        verbose_name = 'enthusiastic',
        default=None,
        blank=False
      
    )
    kind = models.CharField(
        choices = kind_choices,
        max_length = 20,
        verbose_name = 'kind',
        default=None,
        blank=False
       
    )
    calm = models.CharField(
        choices = Calm_choices,
        max_length = 20,
        verbose_name = 'calm',
        default=None,
        blank=False
    
    )
    
    class Meta:
        verbose_name= 'step_1'
        ordering = ['user_id']
    def __str__(self):
        return self.title
    
    
        
# ---------------------------------------------- Features Selection --------------------------
class step_2(models.Model):
    title = models.CharField(
        max_length = 20, 
        editable=False,
        default = 'step2'
    )
    
    user_id = models.ForeignKey(
        User,
        default = 1,
        on_delete=models.CASCADE
    )
    
    features = MultiSelectField(choices=features_choices,
                                 min_choices=3,
                                 max_length=200)


# ----------------------------------------------  countries name -------------------------------
class country_name(models.Model):
    # title = models.CharField(
    #     max_length = 20,
    #     editable = False,
    #     default = 'country_name'
    # )
    
    country_name = models.CharField(
        blank=False,
        max_length = 50,
        default = country_name[0][0],
        choices = country_name
    )
    #country_rating = models.IntegerField(default = 0,validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return self.country_name
    
    class Meta:
        verbose_name = "country_name"

# ----------------------------------------------  user rating -------------------------------
class user_rate(models.Model):
    title = models.CharField(
        max_length = 20,
        editable = False,
        default = 'user_rate'
    )
    
    user_id = models.ForeignKey(
        User,
        default = 1,
        related_name='current_user',
        on_delete=models.CASCADE
    )
    
    countries_name_id = models.ForeignKey(
        country_name,
        blank=False,
        default = 1,
        on_delete = models.CASCADE
    )
    country_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    def __str__(self):
        return "{}_{}".format(self.user_id.username,self.countries_name_id.country_name)
    
    class Meta:
        unique_together = (('countries_name_id', 'user_id'),)
        verbose_name = "user_rate"

    



# class step_3(models.Model):
#     title = models.CharField(
#         max_length = 20, 
#         editable=False,
#         default = 'step3'
#     )
    
#     # user_rate = models.ManyToManyField(
#     #     User
#     # )
    
#     user_id= models.ForeignKey(
#         User,
#         default = 1,
#         related_name='current_user',
#         on_delete=models.CASCADE
#     )
    
#     countries = CountryField(multiple = True,
#                            default=None,
                           
#                             blank=False)
    
#     country_rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    
#     class Meta:
#         ordering = ["country_rate"]
#         verbose_name = 'step_3'
#     def __str__(self):
#         return self.title


