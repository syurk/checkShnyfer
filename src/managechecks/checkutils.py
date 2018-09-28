"""
checkutils.py
This is a set of utility functions to include for views to interact with Checks in the DB.
"""

from datetime import datetime
from django.utils import timezone
from .models import Check

def getCheckById(id):
    """
    Returns whether a check exists with specified id.
    """
    if not id:
        return None
    return Check.objects.get(check_id=int(id))

def addCheckToDB(request):
    c = Check()
    c.name = request.POST.get("fullname")
    c.written_date = timezone.make_aware(datetime.strptime(request.POST.get("checkdate"), "%Y-%m-%d"))
    c.amount = request.POST.get("dollaramount")
    c.routing_no = request.POST.get("routingnumber")
    c.account_no = request.POST.get("accountnumber")
    c.check_no = request.POST.get("checknumber")
    c.save()

def editCheckInDB(request, check):
    check.name = request.POST.get("fullname")
    check.written_date = timezone.make_aware(datetime.strptime(request.POST.get("checkdate"), "%Y-%m-%d"))
    check.amount = request.POST.get("dollaramount")
    check.routing_no = request.POST.get("routingnumber")
    check.account_no = request.POST.get("accountnumber")
    check.check_no = request.POST.get("checknumber")
    check.save()

def handleManageCheckRequest(request):
    check = getCheckById(request.POST.get("id"))
    addCheckToDB(request) if check is None else editCheckInDB(request, check)