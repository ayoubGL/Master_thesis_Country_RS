# Generated by Django 2.2.2 on 2019-07-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0006_auto_20190717_1845'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author_2',
        ),
        migrations.AlterField(
            model_name='step_1',
            name='age',
            field=models.CharField(choices=[('under_18', 'under_18'), ('18_24', '18_24'), ('25_35', '25_35'), ('35_45', '35_45'), ('45_55', '45_55'), ('Over_55', 'Over_55')], default='under_18', max_length=20, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='calm',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Strongly Disagree', max_length=20, verbose_name='calm'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='enthusiastic',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Strongly Disagree', max_length=20, verbose_name='enthusiastic'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Refuse to disclose', 'Refuse to disclose')], default='Male', max_length=20, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='imaginative',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Strongly Disagree', max_length=20, verbose_name='imaginative'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='kind',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Strongly Disagree', max_length=20, verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='step_1',
            name='organized',
            field=models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], default='Strongly Disagree', max_length=20, verbose_name='organized'),
        ),
    ]
