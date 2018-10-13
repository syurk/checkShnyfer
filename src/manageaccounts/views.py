from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Account
from .accountutils import handleManageAccountRequest

from django.contrib.auth.decorators import login_required

app_name = 'manageaccounts_app'

@login_required
def index(request):
    return render(request, 'manageaccounts/index.html', {"accounts": Account.objects.order_by('-account_id').exclude(name="")})

@login_required
def addaccounts(request):
    return render(request, 'manageaccounts/addaccts.html')

@login_required
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