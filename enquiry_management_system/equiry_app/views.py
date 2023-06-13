from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import enq_form_tb,Meeting_Links_TB
from datetime import datetime

# Create your views here.

def home(request):
    if request.method == "POST":
        return HttpResponse('Done')
    return render(request,'index.html')

def submit_func(request):
    
    if request.method == "POST":
        print("in 14"*10)
        name = request.POST.get('name')
        email = request.POST.get('email')
        qualification = request.POST.get('qual')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        meet_time = request.POST.get('meet_time')
        meet_time = datetime.fromisoformat(meet_time)
        course = request.POST.get('courses')
        print(course*10)
        comment = request.POST.get('comment')

        enq_obj = enq_form_tb(name=name,email=email,qualification=qualification,address=address,ph_num = phone,course=course,comment=comment,meeting_time=meet_time)
        
        try:
            m_obj=Meeting_Links_TB.objects.get(course=course,meeting_time=meet_time)
            status = "Success"
        except:
            status = "Warning"

        link = m_obj.link
        # enq_obj.save()
        return JsonResponse({'status':status,'link':link},safe=False)
    
    
def add_meeting(request):
    if request.method == "POST":
        course = request.POST.get('courses')
        m_link = request.POST.get('Link')
        meet_time = request.POST.get('meeting_time')
        date_obj = datetime.fromisoformat(meet_time)
        mtb_obj = Meeting_Links_TB(course=course,link=m_link,meeting_time=date_obj)
        mtb_obj.save()
        print("35"*20)
        return redirect(home)
    return render(request,'add_time.html')