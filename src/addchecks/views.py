from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Check

def index(request):
    with open('addchecks/addchecks.html', 'r') as myfile:
        data = myfile.read()
    return HttpResponse(data)

def viewchecks(request):
    addCheckToDB(request)
    return HttpResponse(', '.join(map(lambda c: checkToString(c),Check.objects.order_by('-written_date'))))

def addCheckToDB(request):
    c = Check()
    c.name = "benji"
    c.written_date = timezone.now()
    c.amount = 0
    c.routing_no = 0
    c.account_no = 0
    c.check_no = 0
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
