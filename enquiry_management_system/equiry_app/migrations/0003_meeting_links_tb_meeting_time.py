# Generated by Django 4.2.1 on 2023-05-09 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equiry_app', '0002_meeting_links_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting_links_tb',
            name='meeting_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
