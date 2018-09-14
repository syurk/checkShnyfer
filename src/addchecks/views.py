from django.shortcuts import render
from django.http import HttpResponse

from .models import Check

def index(request):
    return HttpResponse("Hello, world.")

def viewchecks(request):
    return HttpResponse(', '.join(map(lambda c: checkToString(c),Check.objects.order_by('-written_date')[:5])))

def checkToString(check):
    return """
    <p>Name: {}</p>
    <p>Date Written: {}</p>
    <p>Amount: {}</p>
    <p>Routing Number: {}</p>
    <p>Account Number: {}</p>
    <p>Check Number: {}</p>
    """.format(c.name, c.written_date, c.amount, c.routing_no, c.account_no, c.check_no)