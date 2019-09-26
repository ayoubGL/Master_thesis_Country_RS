from django.contrib import admin
from thesis_app.models import step_1,step_2,country_name,user_rate,usabilitySurvey,user_result,evaluate_result

    
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
import csv
from django.http import HttpResponse

def export_as_csv_action(description="Export selected objects as CSV file", fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        opts = modeladmin.model._meta
        field_names = [field.name for field in opts.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

        # opts = modeladmin.model._meta
        # field_names = set([field.name for field in opts.fields])

        # if fields:
        #     fieldset = set(fields)
        #     field_names = field_names & fieldset

        # elif exclude:
        #     excludeset = set(exclude)
        #     field_names = field_names - excludeset

        # response = HttpResponse(content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename=%s.csv' % str(opts).replace('.', '_')

        # writer = csv.writer(response)

        # if header:
        #     writer.writerow(list(field_names))
        # for obj in queryset:
        #     writer.writerow([str(getattr(obj, field)).encode("utf-8","replace") for field in field_names])

        # return response

    export_as_csv.short_description = description
    return export_as_csv
# export csv 



class UserAdmin(UserAdmin):
    actions = [export_as_csv_action("CSV Export")]

class step_1Admin(admin.ModelAdmin):
    list_display = ('user_id','created','gender','age','country','imaginative','organized','enthusiastic','kind','calm')
    actions = [export_as_csv_action("CSV Export")]
        
    
    
class step_2Admin(admin.ModelAdmin):
    list_display = ('user_id','created','features')
    actions = [export_as_csv_action("CSV Export")]

class user_rateAdmin(admin.ModelAdmin):
    list_display = ('user_id','created','countries_name_id','country_rating')
    actions = [export_as_csv_action("CSV Export")]

class usabilitySurveyAdmin(admin.ModelAdmin):
    list_display = ('user_id','created','usage_frequency','system_complexity','usage_ease',
                    'need_help','functions_integrated','system_inconsistency','learn_to_use','system_inconvenient','confident_level','learning_before','comment')
    actions = [export_as_csv_action("CSV Export")]

class user_resultAdmin(admin.ModelAdmin):
    list_display = ('user_id','countries_name','algorithm','created')
    actions = [export_as_csv_action("CSV Export")]

class evaluate_resultAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'created', 'appealed_list','bad_suggestions','similar_result','varied_selection','wider_preference','better_reflection','more_personalized','more_mainstream','better_help','recommended_list','not_expect','familiar_list','surprising_list','fewer_suggestions')
    actions = [export_as_csv_action("CSV Export")]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(step_1,step_1Admin)
admin.site.register(step_2,step_2Admin)
admin.site.register(country_name)
admin.site.register(user_rate,user_rateAdmin)
admin.site.register(usabilitySurvey,usabilitySurveyAdmin)
admin.site.register(user_result,user_resultAdmin)
admin.site.register(evaluate_result,evaluate_resultAdmin)