# Generated by Django 2.2.2 on 2019-08-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0049_auto_20190818_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step_1',
            name='age',
            field=models.CharField(choices=[('under_18', 'Under 18'), ('b18_24', '18 24'), ('b25_35', '25 35'), ('b35_45', '35 45'), ('b45_55', '45 55'), ('bover_55', 'Over 55')], default=None, max_length=40, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='calm',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='calm'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='enthusiastic',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='enthusiastic'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('refuse_to_disc', 'Refuse to disclose')], default=None, max_length=20, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='imaginative',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='imaginative'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='kind',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='organized',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='organized'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='confident_level',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='confident_level'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='functions_integrated',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='functions_integrated'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='learn_to_use',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='learn_to_use'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='learning_before',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='learning_before'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='need_help',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='need_help'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='system_complexity',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='system_complexity'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='system_inconsistency',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='system_inconsistency'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='system_inconvenient',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='system_inconvenient'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='usage_ease',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='usage_ease'),
        ),
        migrations.AlterField(
            model_name='usabilitysurvey',
            name='usage_frequency',
            field=models.CharField(choices=[('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Natural', 'Natural'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=20, verbose_name='usage_frequency'),
        ),
    ]