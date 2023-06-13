from django.db import models
from django.utils import timezone

# Create your models here.

class enq_form_tb(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    ph_num = models.IntegerField()
    meeting_time = models.DateTimeField(default=timezone.now)
    course = models.CharField(max_length=20)
    comment = models.CharField(max_length=100)


class Meeting_Links_TB(models.Model):
    course = models.CharField(max_length=20)
    meeting_time = models.DateTimeField(default=timezone.now)
    link = models.URLField(max_length=200)


    