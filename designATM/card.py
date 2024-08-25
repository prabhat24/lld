
from user_bank_account import BankAccount



class Card:

    def __init__(self, account: BankAccount, cvv: str):
        self.bank_account = account
        self.cvv = cvv
        self.pin = "0000"
    
    def set_new_pin(self, pin):
        self.pin = pin

    def read_card_details(self):
        print("=====CARD DETAILS=====")
        print(f"username: {self.bank_account.user.username}")
        print(f"customer ID {self.bank_account.user.cid}")
        print(f"account no: {self.bank_account.account_id}")
        print("======================")

    