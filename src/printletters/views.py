from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.utils.encoding import smart_str
from managechecks.models import Check

from datetime import datetime, timedelta

def index(request):
    all_ids_string = ''
    goaldates = [
        timezone.make_aware(datetime.now() - timedelta(days=10)).date(),
        timezone.make_aware(datetime.now() - timedelta(days=20)).date(),
        timezone.make_aware(datetime.now() - timedelta(days=30)).date()
        ]

    checks_to_print = []
    checks_not_to_print = []
    for check in Check.objects.order_by('-written_date'):
        if check.written_date.date() in goaldates:
            all_ids_string += 'id=' + str(check.check_id) + '&'
            checks_to_print.append(check)
        else:
            checks_not_to_print.append(check)
    all_ids_string = all_ids_string[:-1]

    context = {
        'checks_to_print': checks_to_print,
        'checks_not_to_print': checks_not_to_print,
        'all_ids_string': all_ids_string
    }
    return render(request, 'printletters/index.html', context)

def viewletter(request):
    goaldates = {
        'secondary': timezone.make_aware(datetime.now() - timedelta(days=20)).date(),
        'terminal': timezone.make_aware(datetime.now() - timedelta(days=30)).date()
    }

    initialchecks = []
    secondarychecks = []
    terminalchecks = []

    for id in request.GET.getlist('id'):
        check = Check.objects.get(check_id=id)
        print(check.written_date.date(), goaldates)

        if check.written_date.date() <= goaldates['terminal']:
            terminalchecks.append(Check.objects.get(check_id=int(id)))
        elif check.written_date.date() <= goaldates['secondary']:
            secondarychecks.append(Check.objects.get(check_id=int(id)))
        else:
            initialchecks.append(Check.objects.get(check_id=int(id)))
    context = {
        'initialchecks': initialchecks,
        'secondarychecks': secondarychecks,
        'terminalchecks': terminalchecks,
    }

    return render(request, 'printletters/letterform.html', context)