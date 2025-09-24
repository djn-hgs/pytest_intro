class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def pay_in_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if amount > self.balance:
            raise OverdrawnError
        self.balance -= amount

    def transfer_money(self, destination, amount):
        self.withdraw_money(amount)
        destination.pay_in_money(amount)


class OverdrawnError(Exception):
    pass