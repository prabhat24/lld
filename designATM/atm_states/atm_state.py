
from abc import ABC, abstractmethod

# from atm import ATM

class ATMState(ABC):

    def __init__(self, atm):
        self.atm = atm

    def insert_card(self, card):
        raise Exception("Something went wrong")


    def read_card(self, card, pin):
        raise Exception("Something went wrong")
    
    def select_operation(self, card, transaction_type):
        raise Exception("Something went wrong")
    
    def withdwaw_cash(self, amount, card_pin):
        raise Exception("Something went wrong")
    
    def display_balance(self, card):
        raise Exception("Something went wrong")
    
    def exit(self):
        
        raise Exception(f"{self.atm.get_state()} Something went wrong")

