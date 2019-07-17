from django.db import models
from django.utils import timezone
from django.conf import settings

  
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
    # ______________ choices ___________
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
    
    
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    gender = models.CharField(
        choices = Gender_choices,
        max_length = 1,
        verbose_name = 'gender'
    )
    
    age = models.CharField(
        choices = Age_choices,
        max_length = 1,
        verbose_name = 'age'
    )
    

# Create your models here.