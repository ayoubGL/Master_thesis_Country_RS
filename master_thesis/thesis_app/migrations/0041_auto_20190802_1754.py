# Generated by Django 2.2.2 on 2019-08-02 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0040_auto_20190802_1726'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user_rate',
            unique_together=set(),
        ),
    ]