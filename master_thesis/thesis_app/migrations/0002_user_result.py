# Generated by Django 2.2.2 on 2019-08-28 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thesis_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='user_result', editable=False, max_length=20)),
                ('countries_name', models.CharField(max_length=100)),
                ('algorithm', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
