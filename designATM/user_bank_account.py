
from user import User


class BankAccount():

    def __init__(self, account_id: str, user: User):
        self.account_id = account_id
        self.user = user
        self.balance = 0

    def get_account_balance(self):
        return self.balance

    def deposite_amount(self, amt):
        self.balance += amt
    

    def withdraw_amount(self, amt):
        self.balance -= amt
    

