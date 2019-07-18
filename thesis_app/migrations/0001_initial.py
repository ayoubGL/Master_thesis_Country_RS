# Generated by Django 2.2.2 on 2019-07-17 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='step_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='step1', editable=False, max_length=70)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Refuse to disclose', 'Refuse to disclose')], max_length=1, verbose_name='gender')),
                ('age', models.CharField(choices=[('under_18', 'under_18'), ('18_24', '18_24'), ('25_35', '25_35'), ('35_45', '35_45'), ('45_55', '45_55'), ('Over_55', 'Over_55')], max_length=1, verbose_name='age')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('imaginative', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=70, verbose_name='imaginative')),
                ('organized', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=70, verbose_name='imaginative')),
                ('enthusiastic', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=80, verbose_name='enthusiastic')),
                ('kind', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=80, verbose_name='kind')),
                ('calm', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=80, verbose_name='kind')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'step_1',
                'ordering': ['user_id'],
            },
        ),
    ]
