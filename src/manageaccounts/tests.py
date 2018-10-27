from django.test import TestCase
from .models import Account
from managechecks.models import Check
import datetime


# Create your tests here.

class AccountTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.JimAcc = Account.objects.create(name="Jim",
                               phone_number="1234567890",
                               routing_no=int("12345"),
                               account_no=int("0987654321"),
                               street_address="1700 Wade Hampton",
                               city="Greenville",
                               state="sc",
                               zip="10293")
        Account.objects.create(name="Alan",
                               phone_number="6789543212",
                               routing_no=int("45678"),
                               account_no=int("6785409123"),
                               street_address="1701 Wade Hampton",
                               city="Gville",
                               state="NC",
                               zip="09234")
#        Check.objects.create(account = cls.JimAcc,
#                             written_date = d,
#                             amount = int("45"),
#                             check_no = int("456"))
#        
    def test_Account(self):
        jim = Account.objects.get(name="Jim")
        alan = Account.objects.get(name="Alan")
        self.assertEqual(jim.name, "Jim")
        self.assertEqual(jim.phone_number, "1234567890")
        self.assertEqual(jim.routing_no, int("12345"))
        self.assertEqual(jim.account_no, int("0987654321"))
        self.assertEqual(jim.street_address, "1700 Wade Hampton")
        self.assertEqual(jim.city, "Greenville")
        self.assertEqual(jim.state, "sc")
        self.assertEqual(jim.zip, "10293")
        self.assertEqual(alan.name, "Alan")
        self.assertEqual(alan.phone_number, "6789543212")
        self.assertEqual(alan.routing_no, int("45678"))
        self.assertEqual(alan.account_no, int("6785409123"))
        self.assertEqual(alan.street_address, "1701 Wade Hampton")
        self.assertEqual(alan.city, "Gville")
        self.assertEqual(alan.state, "NC")
        self.assertEqual(alan.zip, "09234")
        
#    def test_Check(self):
#        chk = Check.objects.get(check_n0=int("456"))
#        self.assertEqual(chk.written_date, second, msg)
        
        
        
        