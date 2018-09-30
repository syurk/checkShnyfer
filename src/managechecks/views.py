from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Check
from .checkutils import handleManageCheckRequest

from django.contrib.auth.decorators import login_required

from manageaccounts.models import Account

app_name = 'managechecks_app'

@login_required
def index(request):
    return render(request, 'managechecks/index.html', {"checks": Check.objects.order_by('-written_date')})

@login_required
def addchecks(request):
    return render(request, 'managechecks/addchecks.html', {"accounts": Account.objects.all()})

def editcheck(request):
    check = Check.objects.get(check_id=request.GET.get('id'))
    return render(request, 'managechecks/editcheck.html',
    {"check": check, "accounts": Account.objects.all(), "datetimestr": check.written_date.strftime('%Y-%m-%d')})

def deletecheck(request):
    id = request.GET.get('id')
    Check.objects.get(check_id=id).delete()
    return HttpResponse()

def submit(request):
    handleManageCheckRequest(request)
    return redirect('../')
