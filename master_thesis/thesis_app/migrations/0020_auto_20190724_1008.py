# Generated by Django 2.2.2 on 2019-07-24 10:08

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0019_auto_20190723_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step_1',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
