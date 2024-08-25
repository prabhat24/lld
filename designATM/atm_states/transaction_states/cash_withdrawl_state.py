from atm_states.atm_state import ATMState
from atm_states.card_ejecting_state import CardEjectingState 

from atm_states.transaction_states.cash_withdrawl_processor import *

class CashWithdrawlState(ATMState):

    def __init__(self, atm, card):
        self.card = card
        super().__init__(atm)

    def withdwaw_cash(self, request_amount, pin):
        if pin != self.card.pin:
            print("Incorrect Pin Entered")
            self.exit()
            return
        elif request_amount > self.atm.get_balance():
            print("Insufficient funds in ATM")
            self.exit()
            return
        elif request_amount > self.card.bank_account.get_account_balance():
            print("Insufficient funds in Account")
            self.exit()
            return
        elif (request_amount % 100 != 0):
            print("Request amount must be multiple of 100")
            self.exit()
            return
        processor = TwoThousandWithdrawlProcessor(self.atm, 
                FiveHundredWithdrawlProcessor(self.atm, 
                        HundredWithdrawlProcessor(self.atm, 
                                None)))
        result = {}
        processor.withdraw(request_amount, result)
        if result:
            self.atm.two_thousand_notes -= result[2000]
            self.atm.five_hundred_notes -= result[500]
            self.atm.hundred_notes -= result[100]
            self.card.bank_account.withdraw_amount(request_amount)
    
    def exit(self):
       self.atm.set_atm_state(CardEjectingState(self.atm))
       self.atm.get_state().eject_card()