# Generated by Django 2.2.2 on 2019-07-28 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0030_auto_20190728_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step_3',
            name='user_rate',
        ),
    ]
