"""
checkutils.py
This is a set of utility functions to include for views to interact with Checks in the DB.
"""

from datetime import datetime
from django.utils import timezone
from .models import Check
from manageaccounts.models import Account

def getCheckById(id):
    """
    Returns whether a check exists with specified id.
    """
    if not id:
        return None
    return Check.objects.get(check_id=int(id))

def addCheckToDB(request):
    Check.objects.create(
        account=Account.objects.get(account_id=request.POST.get("account")),
        written_date=timezone.make_aware(datetime.strptime(request.POST.get("checkdate"), "%Y-%m-%d")),
        amount=request.POST.get("dollaramount"),
        check_no=request.POST.get("checknumber"))

def editCheckInDB(request, check):
    check.written_date = timezone.make_aware(datetime.strptime(request.POST.get("checkdate"), "%Y-%m-%d"))
    check.amount = request.POST.get("dollaramount")
    check.check_no = request.POST.get("checknumber")
    check.account = Account.objects.get(account_id=request.POST.get("account"))

    check.save()

def handleManageCheckRequest(request):
    check = getCheckById(request.POST.get("id"))
    addCheckToDB(request) if check is None else editCheckInDB(request, check)