# Generated by Django 2.2.2 on 2019-07-27 15:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0025_auto_20190727_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries_name',
            name='country_rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
