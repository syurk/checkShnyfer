from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    routing_no = models.PositiveIntegerField('routing number')
    account_no = models.PositiveIntegerField('account number')
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)