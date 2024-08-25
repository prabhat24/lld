from atm import ATM
from card import Card
from user_bank_account import BankAccount
from user import User

from atm_states.transaction_states.transaction_types import TransactionType

atm = ATM("123234")
atm.deposite_cash_in_atm(10, 20, 30)
if __name__ == "__main__":
    
    transaction = atm.init()

    # onboarding user, card and his bank account
    user = User("Prabhat Katiyar", "+916361182047", "flt-23, lone1, line2")
    user_account = BankAccount(account_id="3422-3233-41314", user=user)
    user_account.deposite_amount(5000)
    card = Card(account=user_account, cvv="311")

    # insert the card inside the atm machine
    transaction.get_state().insert_card(card)

    transaction.get_state().read_card()
    transaction.get_state().select_operation(TransactionType.CASH_WITHDRAWAL)
    transaction.get_state().withdwaw_cash(4700, "0000")

    transaction.get_state().exit()

