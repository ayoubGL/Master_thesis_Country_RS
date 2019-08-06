# Generated by Django 2.2.2 on 2019-07-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0017_auto_20190723_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step_1',
            name='age',
            field=models.CharField(choices=[('under_18', 'under_18'), ('18_24', '18_24'), ('25_35', '25_35'), ('35_45', '35_45'), ('45_55', '45_55'), ('Over_55', 'Over_55')], default='Unspecified', max_length=40, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='calm',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Unspecified', max_length=20, verbose_name='calm'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='enthusiastic',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Unspecified', max_length=20, verbose_name='enthusiastic'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Refuse to disclose', 'Refuse to disclose')], default='Unspecified', max_length=20, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='imaginative',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Unspecified', max_length=20, verbose_name='imaginative'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='kind',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Unspecified', max_length=20, verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='organized',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Unspecified', max_length=20, verbose_name='organized'),
        ),
    ]