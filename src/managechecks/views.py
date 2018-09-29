from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Check
from .checkutils import handleManageCheckRequest

def index(request):
    return render(request, 'managechecks/index.html', {"checks": Check.objects.order_by('-written_date').exclude(name="")})

def addchecks(request):
    return render(request, 'managechecks/addchecks.html')

def editcheck(request):
    check = Check.objects.get(check_id=request.GET.get('id'))
    return render(request, 'managechecks/editcheck.html',
    {"check": check, "datetimestr": check.written_date.strftime('%Y-%m-%d')})

def deletecheck(request):
    id = request.GET.get('id')
    Check.objects.get(check_id=id).delete()
    return HttpResponse()

def submit(request):
    handleManageCheckRequest(request)
    return redirect('../')
