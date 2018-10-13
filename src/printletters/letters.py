from managechecks.models import Check

from io import BytesIO, StringIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import zipfile

from datetime import datetime

def currentdatestr():
    return datetime.strftime(datetime.now().date(), '%d-%m-%Y')

def filenameFromCheckId(id):
    c = Check.objects.get(check_id=id)
    return 'letters/%d-%s-%s.pdf' % (c.check_no, c.account.name, currentdatestr())

def zipname():
    return 'letters/%s.zip' % (currentdatestr())

def checkdate(check):
    return datetime.strftime(check.written_date, '%d/%m/%Y')

def writeLetter(canvas, check):
    account = check.account
    canvas.drawString(inch * 3, inch * 10.5, "NOTICE OF DISHONORED CHECK")
    canvas.drawString(inch * 1, inch * 10, 'CheckShnyfer')
    canvas.drawString(inch * 1, inch * 9.5, '1700 Wade Hampton Blvd.')
    canvas.drawString(inch * 1, inch * 9, 'Greenville, SC')
    canvas.drawString(inch * 1, inch * 8.5, checkdate(check))
    canvas.drawString(inch * 1, inch * 7.5, account.name)
    canvas.drawString(inch * 1, inch * 7, account.street_address)
    canvas.drawString(inch * 1, inch * 6.5, '%s, %s %s' % (account.city, account.state, account.zip))
    canvas.drawString(inch * 1.5, inch * 5.75, 'Dear %s,' % (account.name))
    canvas.drawString(inch*1, inch*5.5, 'I am writing to inform you that check #%d dated %s, in the amount of $%d,' % (check.check_no, checkdate(check), check.amount))
    canvas.drawString(inch*1, inch*5.25, 'has been returned to me. I realize that such mishaps can occur and am confident that you')
    canvas.drawString(inch*1, inch*5, 'will rectify this matter immediately. Accordingly, I ask that you please mail (or deliver')
    canvas.drawString(inch*1, inch*4.75, 'in person) a new payment in the original amount plus the bank’s returned-check fee of')
    canvas.drawString(inch*1, inch*4.5, '$%d to the following address: 1700 Wade Hampton Blvd. Please make your payment' % (check.amount))
    canvas.drawString(inch*1, inch*4.25, 'in cash, certified check, cashier’s check or money order only. It is imperative')
    canvas.drawString(inch*1, inch*4, 'that you do so without delay. If funds are now available in your account and you')
    canvas.drawString(inch*1, inch*3.75, 'would like me to redeposit the check, please let me know as soon as possible.')
    canvas.drawString(inch*1, inch*3.5, 'You may contact us at 515-SHN-YFYS. If you have already sent replacement funds,')
    canvas.drawString(inch*1, inch*3.25, 'please disregard this letter. Thank you for your prompt attention to this matter.')
    canvas.drawString(inch*1.5, inch*2.75, 'CheckShnyfer Inc.')

def generateLetter(check):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    writeLetter(p, check)

    p.showPage()
    p.save()

    with open(filenameFromCheckId(check.check_id), 'wb') as f:
        f.write(buffer.getvalue())

    return buffer

def generateCheck(checks):
    buf = StringIO()
    letters = {}

    for check in checks:
        letters[check.check_id] = generateLetter(check)

    zip_archive = zipfile.ZipFile(zipname(), mode='w', compression=zipfile.ZIP_DEFLATED)
    for id, letter in letters.items():
        zip_archive.write(filenameFromCheckId(id))
    zip_archive.close()

    with open('test.zip', 'w') as f:
        f.write(buf.getvalue())

    buf.flush()
    value = buf.getvalue()
    buf.close()

    return value