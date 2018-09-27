from django.db import models

class Check(models.Model):
    name = models.CharField(max_length=150)
    written_date = models.DateTimeField('date written')
    amount = models.PositiveIntegerField('amount')
    routing_no = models.PositiveIntegerField('routing number')
    account_no = models.PositiveIntegerField('account number')
    check_no = models.PositiveIntegerField('check number')
