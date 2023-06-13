from django.contrib import admin
from .models import enq_form_tb,Meeting_Links_TB


# Register your models here.


@admin.register(enq_form_tb)
class enq_form_tb(admin.ModelAdmin):
    list_display = ['id','name','email','qualification','address','ph_num','meeting_time','course','comment']


@admin.register(Meeting_Links_TB)
class Meeting_Links_TB(admin.ModelAdmin):
    list_display = ['course','meeting_time','link']


