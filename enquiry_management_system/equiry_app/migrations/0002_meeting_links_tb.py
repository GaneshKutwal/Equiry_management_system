# Generated by Django 4.2.1 on 2023-05-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equiry_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_Links_TB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=20)),
                ('link', models.URLField()),
            ],
        ),
    ]