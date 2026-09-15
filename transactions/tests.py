from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import BankAccountType, UserBankAccount
from .models import Transaction
from decimal import Decimal

User = get_user_model()

class TransactionTest(TestCase):
    def test_deposit_transaction(self):
        user = User.objects.create_user(email="trans@bank.com", password="pass")
        acc_type = BankAccountType.objects.create(
            name="Savings", maximum_withdrawal_amount=10000,
            annual_interest_rate=5, interest_calculation_per_year=12
        )
        account = UserBankAccount.objects.create(
            user=user, account_type=acc_type, account_no=200001,
            gender="M", balance=Decimal(1000)
        )
        trans = Transaction.objects.create(
            account=account, amount=Decimal(500), balance_after_transaction=Decimal(1500),
            transaction_type=1
        )
        self.assertEqual(trans.amount, Decimal(500))
        self.assertEqual(account.account_no, 200001)
