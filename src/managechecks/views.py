from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from datetime import datetime

from .models import Check

def index(request):
    return render(request, 'managechecks/index.html', {"checks": Check.objects.order_by('-written_date').exclude(name="")})

def addchecks(request):
    return render(request, 'managechecks/addchecks.html')

def editcheck(request):
    check = Check.objects.get(check_id=request.GET['id'][0])
    return render(request, 'managechecks/editcheck.html',
    {"check": check, "datetimestr": check.written_date.strftime('%Y-%m-%d')})

def submit(request):
    addCheckToDB(request)
    return render(request, "managechecks/submitcheck.html")

def addCheckToDB(request):
    c = Check()
    c.name = request.POST.get("fullname")
    c.written_date = timezone.make_aware(datetime.strptime(request.POST.get("checkdate"), "%Y-%m-%d"))
    c.amount = request.POST.get("dollaramount")
    c.routing_no = request.POST.get("routingnumber")
    c.account_no = request.POST.get("accountnumber")
    c.check_no = request.POST.get("checknumber")
    c.save()
