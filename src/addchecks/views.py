from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from datetime import datetime

from .models import Check

def index(request):
    return render(request, 'addchecks/addchecks.html')

def submit(request):
    addCheckToDB(request)
    return HttpResponse("Submitted check. <a href='../viewchecks'>Click here to view all checks.</a>")

def viewchecks(request):
    return render(request, "addchecks/viewchecks.html", {"checks": Check.objects.order_by('-written_date').exclude(name="")})

def addCheckToDB(request):
    c = Check()
    c.name = request.POST.get("fullname")
    c.written_date = timezone.make_aware(datetime.strptime(request.POST.get("checkdate"), "%Y-%m-%d"))
    c.amount = request.POST.get("dollaramount")
    c.routing_no = request.POST.get("routingnumber")
    c.account_no = request.POST.get("accountnumber")
    c.check_no = request.POST.get("checknumber")
    c.save()
