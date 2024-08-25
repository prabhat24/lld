from .atm_state import ATMState
from atm_states.transaction_states.transaction_types import TransactionType
from atm_states.transaction_states.balance_check_state import BalanceCheckState
from atm_states.transaction_states.cash_withdrawl_state import CashWithdrawlState
from atm_states.card_ejecting_state import CardEjectingState


class SelectOperationState(ATMState):


    def __init__(self, atm, card):
        self.card = card
        super().__init__(atm)
        self.show_operations()
    


    def show_operations(self):
        print("Please select the Operation")
        TransactionType.show_all_transaction_types()

    def select_operation(self, transaction_state):
        if transaction_state == TransactionType.BALANCE_CHECK:
            print(f"selected operation: {TransactionType.BALANCE_CHECK.value}")
            self.atm.set_atm_state(BalanceCheckState(self.atm, self.card))
            return
        elif transaction_state == TransactionType.CASH_WITHDRAWAL:
            print(f"selected operation: {TransactionType.CASH_WITHDRAWAL.value}")
            self.atm.set_atm_state(CashWithdrawlState(self.atm, self.card))
            return
        print("Unknown Option Selected")
        self.exit()

    def exit(self):
        self.atm.set_atm_state(CardEjectingState(self.atm))
        self.atm.get_state().eject_card()

