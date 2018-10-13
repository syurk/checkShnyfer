from django.shortcuts import render
from django.utils import timezone
from managechecks.models import Check

from datetime import datetime, timedelta

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

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

def generateCheck(check):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(100, 100, "Hello world.")

    p.showPage()
    p.save()
    return buffer

def download(request):
    checks = request.GET.getlist('id')
    letters = []
    for check in checks:
        letters.append(generateCheck(check))
    return index(request)