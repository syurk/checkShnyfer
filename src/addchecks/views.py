from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

import datetime

from .models import Check

def index(request):
    return render(request, 'addchecks/addchecks.html')

def submit(request):
    addCheckToDB(request)
    return HttpResponse("Submitted check. <a href='../viewchecks'>Click here to view all checks.</a>")

def viewchecks(request):
    return HttpResponse(', '.join(map(lambda c: checkToString(c),Check.objects.order_by('-written_date'))))

def addCheckToDB(request):
    c = Check()
    c.name = request.POST.get("fullname")
    c.written_date = request.POST.get("checkdate")
    c.amount = request.POST.get("dollaramount")
    c.routing_no = request.POST.get("routingnumber")
    c.account_no = request.POST.get("accountnumber")
    c.check_no = request.POST.get("checknumber")
    c.save()

def checkToString(check):
    return """
    <h3>Name: {}</h3>
    <h4>Date Written: {}</h4>
    <h4>Amount: {}</h4>
    <p>Routing Number: {}</p>
    <p>Account Number: {}</p>
    <p>Check Number: {}</p>
    </hr>
    """.format(check.name, check.written_date, check.amount, check.routing_no, check.account_no, check.check_no)
