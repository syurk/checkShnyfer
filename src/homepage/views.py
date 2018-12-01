from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)
