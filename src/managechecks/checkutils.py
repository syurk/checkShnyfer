"""
checkutils.py
This is a set of utility functions to include for views to interact with Checks in the DB.
"""

from datetime import datetime
from django.utils import timezone
from .models import Check
from manageaccounts.models import Account

def addCheckToDB(written_date, amt, check_no, account):
    Check.objects.create(
        written_date=written_date,
        amount=amt,
        check_no=check_no,
        account=account)

def editCheckInDB(check, written_date, amt, check_no, account):
    check.written_date = written_date
    check.amount = amt
    check.check_no = check_no
    check.account = account

    check.save()

def handleManageCheckRequest(request):
    check = Check.objects.get(check_id=int(request.POST.get("id")))
    written_date = timezone.make_aware(datetime.strptime(request.POST.get("checkdate"), "%Y-%m-%d"))
    amt = POST.get("dollaramount")
    check_no = request.POST.get("checknumber")
    account = Account.objects.get(account_id=request.POST.get("account"))

    addCheckToDB(written_date, amt, check_no, account) if check is None else editCheckInDB(check, written_date, amt, check_no, account)