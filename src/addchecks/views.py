from django.shortcuts import render
from django.http import HttpResponse

from .models import Check

def index(request):
    return HttpResponse("Hello, world.")

def viewchecks(request):
    return HttpResponse(', '.join(map(lambda c: checkToString(c),Check.objects.order_by('-written_date'))))

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