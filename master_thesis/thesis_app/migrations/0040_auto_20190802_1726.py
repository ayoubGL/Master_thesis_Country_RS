# Generated by Django 2.2.2 on 2019-08-02 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0039_auto_20190802_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_rate',
            name='countries_name_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='thesis_app.country_name'),
        ),
    ]