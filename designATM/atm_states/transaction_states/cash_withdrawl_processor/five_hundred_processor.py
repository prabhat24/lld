from abc import ABC, abstractmethod
from .withdrawl_processor import WithdrawlProcessor

class FiveHundredWithdrawlProcessor(WithdrawlProcessor):

    def withdraw(self, amount, result):
        actual_notes_to_deduct = 0
        max_notes_to_deduct = amount // 500
        actual_notes_to_deduct = min(self.atm.get_hundred_notes(), max_notes_to_deduct)
        amount_to_be_processed_by_next_processor = amount - actual_notes_to_deduct * 500
        result["500"] = actual_notes_to_deduct
        if amount_to_be_processed_by_next_processor:
            super().withdraw(amount_to_be_processed_by_next_processor, result)
        return result