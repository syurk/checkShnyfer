from django.test import TestCase
from .models import Check
from manageaccounts.models import Account
import datetime
from django.utils import timezone
from .checkutils import editCheckInDB, addCheckToDB

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
        self.AndyAcc = Account.objects.create(name="Andy",
                               phone_number="0987654321",
                               routing_no=int("54321"),
                               account_no=int("1234567890"),
                               street_address="2300 Hade Wampton",
                               city="Redville",
                               state="nc",
                               zip="92314")
        self.today = timezone.make_aware(datetime.datetime(year=2018, month=11, day=10), timezone.utc)
#        
    def test_editCheck(self):
        check = Check.objects.create(account=self.JimAcc,
                            written_date=self.today,
                            amount=123.45,
                            check_no=12345,
                            recipient='Walmart')
        edited = {
            "amount": 987.65,
            "check_no": 98765,
            "written_date": timezone.make_aware(datetime.datetime(year=2020, month=1, day=31), timezone.utc),
            "account": self.AndyAcc,
            "recipient": 'Target'
            }
        
        self.assertNotEqual(check.written_date, edited["written_date"])
        self.assertNotEqual(check.amount, edited["amount"])
        self.assertNotEqual(check.check_no, edited["check_no"])
        self.assertNotEqual(check.account, edited["account"])
        self.assertNotEqual(check.recipient, edited["recipient"])

        editCheckInDB(check, edited["written_date"], edited["amount"], edited["check_no"], edited["account"], recipient["recipient"])

        self.assertEqual(check.written_date, edited["written_date"])
        self.assertEqual(check.amount, edited["amount"])
        self.assertEqual(check.check_no, edited["check_no"])
        self.assertEqual(check.account, edited["account"])
        self.assertEqual(check.recipient, edited["recipient"])
        
    def test_addCheck(self):
        self.assertEqual(Check.objects.all().count(), 0)
        check_info = {
            "amount": 987.65,
            "check_no": 98765,
            "written_date": timezone.make_aware(datetime.datetime(year=2020, month=1, day=31), timezone.utc),
            "account": self.AndyAcc
            }

        addCheckToDB(check_info["written_date"], check_info["amount"], check_info["check_no"], check_info["account"])

        self.assertEqual(Check.objects.all().count(), 1)

        check = Check.objects.first()
        self.assertEqual(check.written_date, check_info["written_date"])
        self.assertEqual(check.amount, check_info["amount"])
        self.assertEqual(check.check_no, check_info["check_no"])
        self.assertEqual(check.account, check_info["account"])
        