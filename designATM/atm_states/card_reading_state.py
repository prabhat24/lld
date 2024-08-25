from .atm_state import ATMState
from .card_ejecting_state import CardEjectingState
from .select_operation_state import SelectOperationState
from card import Card

class CardReadingState(ATMState):

    def __init__(self, atm, card):
        self.card: Card = card
        super().__init__(atm)

    def read_card(self):
        print("reading card")
        self.card.read_card_details()
        print("read card details")
        
        #
        # validate card details   
        is_validated = self.validate_card()
        #
        if is_validated:
            print("Card Validated")
            self.atm.set_atm_state(SelectOperationState(self.atm, self.card))
        else:
            print("Invalid Card")
            self.atm.set_atm_state(CardEjectingState(self.atm))

    def validate_card(self):
        # 
        print("validating card")
        # 
        return True
    
    def exit(self):
        print("user terminated the transaction")
        self.atm.set_atm_state(CardEjectingState(self.atm))
        self.atm.get_state().eject_card()