# Generated by Django 4.2.1 on 2023-05-09 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equiry_app', '0003_meeting_links_tb_meeting_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='enq_form_tb',
            name='meeting_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
