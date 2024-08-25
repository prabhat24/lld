
from .atm_state import ATMState


class CardEjectingState(ATMState):

    def eject_card(self):
        from .ready_state import ReadyState
        print("CARD EJECTED: please collect your card")
        self.atm.set_atm_state(ReadyState(self.atm))

    