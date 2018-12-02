"""
checkutils.py
This is a set of utility functions to include for views to interact with Checks in the DB.
"""

from datetime import datetime
from django.utils import timezone
from .models import Check
from manageaccounts.models import Account

def addCheckToDB(written_date, amt, check_no, account, recipient):
    Check.objects.create(
        written_date=written_date,
        amount=amt,
        check_no=check_no,
        account=account,
        recipient=recipient)

def editCheckInDB(check, written_date, amt, check_no, account, recipient):
    check.written_date = written_date
    check.amount = amt
    check.check_no = check_no
    check.account = account
    check.recipient = recipient

    check.save()

def handleManageCheckRequest(request):
    id_str = request.POST.get("id")
    written_date = timezone.make_aware(datetime.strptime(request.POST.get("checkdate"), "%Y-%m-%d"))
    amt = request.POST.get("dollaramount")
    check_no = request.POST.get("checknumber")
    account = Account.objects.get(account_id=request.POST.get("account"))
    recipient = request.POST.get("recipient")

    if id_str:
        check = Check.objects.get(check_id=int(id_str))
        editCheckInDB(check, written_date, amt, check_no, account, recipient)
    else:
        addCheckToDB(written_date, amt, check_no, account, recipient)