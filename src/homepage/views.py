from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Hello')
    context = {}
    template = 'home.html';
    return render(request, template,context )
