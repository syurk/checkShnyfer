from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    with open('addchecks.html', 'r') as myfile:
        data = myfile.read()
    return HttpResponse(data)
