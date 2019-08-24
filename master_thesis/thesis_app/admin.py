from django.contrib import admin
from thesis_app.models import step_1,step_2,country_name,user_rate,UsabilitySurvey

# Register your models here.


class step_1Admin(admin.ModelAdmin):
    list_display = ('user_id','created','gender','age','country','imaginative','organized','enthusiastic','kind','calm')

class step_2Admin(admin.ModelAdmin):
    list_display = ('user_id','created','features')

class user_rateAdmin(admin.ModelAdmin):
    list_display = ('user_id','created','countries_name_id','country_rating')

class UsabilitySurveyAdmin(admin.ModelAdmin):
    list_display = ('user_id','created','email','usage_frequency','system_complexity','usage_ease',
                    'need_help','functions_integrated','system_inconsistency','learn_to_use','system_inconvenient','confident_level','learning_before')

admin.site.register(step_1,step_1Admin)
admin.site.register(step_2,step_2Admin)
admin.site.register(country_name)
admin.site.register(user_rate,user_rateAdmin)
admin.site.register(UsabilitySurvey,UsabilitySurveyAdmin)