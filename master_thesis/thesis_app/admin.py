from django.contrib import admin
from thesis_app.models import step_1,step_2,country_name,user_rate

# Register your models here.
admin.site.register(step_1)
admin.site.register(step_2)
#admin.site.register(step_3)
admin.site.register(country_name)
admin.site.register(user_rate)