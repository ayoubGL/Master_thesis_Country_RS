# Generated by Django 2.2.2 on 2019-08-28 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0003_auto_20190828_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_result',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
