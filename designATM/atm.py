from uuid import uuid4

from atm_states.ready_state import ReadyState

class ATM:
    
    def __init__(self, machine_id):
        self.__machine_id = machine_id
        self.set_atm_state(ReadyState(self))
        self.txn = None
        self.balance = 0
        self.two_thousand_notes = 0
        self.five_hundred_notes = 0
        self.hundred_notes = 0
    
    
    def init(self):
        # return a new unique transactionId
        self.txn = uuid4()
        return self
    
    def deposite_cash_in_atm(self, 
            two_thousand_notes,
            five_hundred_notes,
            hundred_notes):
        amt = two_thousand_notes * 2000 + five_hundred_notes * 500 + hundred_notes * 100
        self.two_thousand_notes += two_thousand_notes
        self.five_hundred_notes += five_hundred_notes
        self.hundred_notes += hundred_notes
        print(f"deposited amount {amt} in atm")
        self.balance = amt

    def get_balance(self):
        return self.balance

    def get_hundred_notes(self):
        return self.hundred_notes

    def get_two_thousand_notes(self):
        return self.two_thousand_notes
    
    def get_five_hundered_notes(self):
        return self.five_hundred_notes

    def set_atm_state(self, state):
        self.__state = state
    
    def get_state(self):
        return self.__state