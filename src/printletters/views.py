from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.utils.encoding import smart_str
from managechecks.models import Check

from datetime import datetime, timedelta

def index(request):
    all_ids_string = ''
    goalday = timezone.make_aware(datetime.now() - timedelta(days=10))
    checks_to_print = []
    checks_not_to_print = []
    for check in Check.objects.order_by('-written_date'):
        if check.written_date.date() == goalday.date():
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
    checks = request.GET.getlist('id')
    checks_to_print = []
    letters = []
    for id in checks:
        checks_to_print.append(Check.objects.get(check_id=int(id)))
    context = { 'checks': checks_to_print }

    return render(request, 'printletters/letterform.html', context)