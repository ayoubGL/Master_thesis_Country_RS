# Generated by Django 2.2.2 on 2019-08-02 18:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thesis_app', '0041_auto_20190802_1754'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user_rate',
            unique_together={('countries_name_id', 'user_id')},
        ),
    ]