"""
accountutils.py
This is a set of utility functions to include for views to interact with Accounts in the DB.
"""

from datetime import datetime
from django.utils import timezone
from .models import Account

def getAccountById(id):
    """
    Returns whether an Account exists with specified id.
    """
    if not id:
        return None
    return Account.objects.get(account_id=int(id))

def addAccountToDB(request):
    a = Account()
    a.name = request.POST.get("name")
    a.phone_number = request.POST.get("phonenumber")
    a.routing_no = request.POST.get("routingnumber")
    a.account_no = request.POST.get("accountnumber")
    a.street_address = request.POST.get("streetaddress")
    a.city = request.POST.get("city")
    a.state = request.POST.get("state")
    a.zip = request.POST.get("zip")
    a.save()

def editAccountInDB(request, account):
    account.name = request.POST.get("name")
    account.phone_number = request.POST.get("phonenumber")
    account.routing_no = request.POST.get("routingnumber")
    account.account_no = request.POST.get("accountnumber")
    account.street_address = request.POST.get("streetaddress")
    account.city = request.POST.get("city")
    account.state = request.POST.get("state")
    account.zip = request.POST.get("zip")
    account.save()

def handleManageAccountRequest(request):
    account = getAccountById(request.POST.get("id"))
    addAccountToDB(request) if account is None else editAccountInDB(request, account)