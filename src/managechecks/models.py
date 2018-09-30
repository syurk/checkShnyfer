from django.db import models

from manageaccounts.models import Account

class Check(models.Model):
    check_id = models.AutoField(primary_key=True)
    account = models.ForeignKey('manageaccounts.Account', on_delete=models.CASCADE)
    written_date = models.DateTimeField('date written')
    amount = models.PositiveIntegerField('amount')
    check_no = models.PositiveIntegerField('check number')
