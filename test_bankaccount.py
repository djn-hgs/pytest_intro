import bankaccount
import pytest

@pytest.fixture
def my_account():
    return bankaccount.BankAccount(balance=100)

@pytest.fixture
def another_account():
    return bankaccount.BankAccount(balance=0)


class TestBankAccount:
    def test_create_bank_account(self, my_account):
        assert my_account.balance == 100


    def test_pay_in_money(self, my_account):
        my_account.pay_in_money(20)
        assert my_account.balance == 120


    def test_withdraw_money(self, my_account):
        my_account.withdraw_money(40)
        assert my_account.balance == 60


    def test_transfer_money(self, my_account, another_account):
        my_account.transfer_money(another_account, 30)
        assert my_account.balance == 70 and another_account.balance == 30

    def test_overdrawn(self, my_account):
        with pytest.raises(bankaccount.OverdrawnError):
            my_account.withdraw_money(400)
