import enum

class TransactionType(enum.Enum):

    CASH_WITHDRAWAL = "WITHDRAW CASH"
    BALANCE_CHECK = "CHECK BALANCE"

    @staticmethod
    def show_all_transaction_types():
        for type in TransactionType:
            print(type.value)
