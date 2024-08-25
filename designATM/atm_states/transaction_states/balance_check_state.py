from atm_states.atm_state import ATMState
from atm_states.card_ejecting_state import CardEjectingState 

class BalanceCheckState(ATMState):

    def __init__(self, atm, card):
        self.card = card
        super().__init__(atm)

    def check_balance(self):
        balance = self.card.bank_account.get_account_balance()
        print(f"user account balance: {balance}")
        return balance
    
    def exit(self):
       self.atm.set_atm_state(CardEjectingState(self.atm))
       self.atm.get_state().eject_card()