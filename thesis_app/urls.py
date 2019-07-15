from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "thesis_app"

urlpatterns = [
    
    path('',views.home, name='home'),
    # path('login/', views.login, name='login'),
    path('survey_page/',views.survey_page, name = 'survey_page')
]
