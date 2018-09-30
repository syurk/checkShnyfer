from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Account
from .accountutils import handleManageAccountRequest

app_name = 'manageaccounts_app'

def index(request):
    return render(request, 'manageaccounts/index.html', {"accounts": Account.objects.order_by('-account_id').exclude(name="")})

def addaccounts(request):
    return render(request, 'manageaccounts/addaccts.html')

def editaccount(request):
    acct = Account.objects.get(account_id=request.GET.get('id'))
    return render(request, 'manageaccounts/editaccts.html',
    {"account": acct})

def deleteaccount(request):
    id = request.GET.get('id')
    Account.objects.get(account_id=id).delete()
    return HttpResponse()

def submit(request):
    handleManageAccountRequest(request)
    return redirect('../')