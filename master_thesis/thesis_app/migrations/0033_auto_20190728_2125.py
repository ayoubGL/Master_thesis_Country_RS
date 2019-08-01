# Generated by Django 2.2.2 on 2019-07-28 21:25

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('thesis_app', '0032_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step_3',
            name='countries',
            field=django_countries.fields.CountryField(default=None, max_length=746, multiple=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
