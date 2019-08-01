from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "thesis_app"

urlpatterns = [
    
    path('',views.home, name='home'),
    path('logout/', views.logout_request, name='lougout'),
    path('login/', views.login_request, name='login'),
    path('personal_info/',views.personal_info, name = 'personal_info'),
    path('features/',views.features, name = 'features'),
    path('countries_rate/',views.countries_rate, name = 'countries_rate'),
    

    
]
