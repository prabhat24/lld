from .atm_state import ATMState

from .card_reading_state import CardReadingState

class ReadyState(ATMState):

    def insert_card(self, card):
        print("card inserted")
        self.atm.set_atm_state(CardReadingState(self.atm, card))

    def exit(self):
        print("not exiting: ATM is already in ready state")