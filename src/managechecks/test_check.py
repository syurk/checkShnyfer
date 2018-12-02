from django.test import TestCase
from .models import Check
from manageaccounts.models import Account
import datetime
from django.utils import timezone

# Create your tests here.

class AccountTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        self.JimAcc = Account.objects.create(name="Jim",
                               phone_number="1234567890",
                               routing_no=int("12345"),
                               account_no=int("0987654321"),
                               street_address="1700 Wade Hampton",
                               city="Greenville",
                               state="sc",
                               zip="10293")
        self.today = timezone.make_aware(datetime.datetime(year=2018, month=11, day=10), timezone.utc)
        Account.objects.create(name="Alan",
                               phone_number="6789543212",
                               routing_no=int("45678"),
                               account_no=int("6785409123"),
                               street_address="1701 Wade Hampton",
                               city="Gville",
                               state="NC",
                               zip="09234")
#        
    def test_Check_decimalamount(self):
        check = Check.objects.create(account=self.JimAcc,
                                     written_date=self.today,
                                     amount=123.42,
                                     check_no=23421,
                                     recipient='BJU')
        self.assertEqual(check.account, self.JimAcc)
        self.assertEqual(check.written_date, self.today)
        self.assertEqual(check.amount, 123.42)
        self.assertEqual(check.check_no, 23421)
        self.assertEqual(check.recipient, 'BJU')
#        
    def test_Check_intamount(self):
        check = Check.objects.create(account=self.JimAcc,
                                     written_date=self.today,
                                     amount=123,
                                     check_no=23421,
                                     recipient='BJU')
        self.assertEqual(check.account, self.JimAcc)
        self.assertEqual(check.written_date, self.today)
        self.assertEqual(check.amount, 123)
        self.assertEqual(check.check_no, 23421)
        self.assertEqual(check.recipient, 'BJU')
        