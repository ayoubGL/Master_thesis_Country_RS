from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf.urls import handler404, handler500
app_name = "thesis_app"

urlpatterns = [
    
    path('',views.home, name='home'),
    path('logout/', views.logout_request, name='lougout'),
    path('login/', views.login_request, name='login'),
    path( 'personal_info/',views.personal_info, name = 'personal_info'),
    path('features/',views.features, name = 'features'),
    path('countries_rate/',views.countries_rate, name = 'countries_rate'),
    path('result/', views.result, name='result'),
    path('UsabilitySurvey/', views.UsabilitySurvey, name='UsabilitySurvey'),
    path('thanks_you/', views.thanks, name='thanks'),
    path('howWorks/', views.howWorks, name='howWorks'),
    path('user_result/', views.redirect_login, name='redirect_login'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = views.error_404
# handler500 = views.error_500