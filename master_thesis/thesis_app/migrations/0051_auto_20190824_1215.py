# Generated by Django 2.2.2 on 2019-08-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0050_auto_20190821_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_rate',
            name='title',
            field=models.CharField(default='User_rate', editable=False, max_length=20),
        ),
    ]