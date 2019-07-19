from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "thesis_app"

urlpatterns = [
    
    path('',views.home, name='home'),
    path('logout/', views.logout_request, name='lougout'),
    path('login/', views.login_request, name='login'),
    path('survey_page/',views.survey_page, name = 'survey_page'),
    path('survey_page_2/',views.survey_page_2, name = 'survey_page_2'),
    
]
