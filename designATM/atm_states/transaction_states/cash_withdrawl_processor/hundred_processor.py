from abc import ABC, abstractmethod

from .withdrawl_processor import WithdrawlProcessor

class HundredWithdrawlProcessor(WithdrawlProcessor):

    def withdraw(self, amount, result):
        actual_notes_to_deduct = 0
        max_notes_to_deduct = amount // 100
        actual_notes_to_deduct = min(self.atm.get_five_hundered_notes(), max_notes_to_deduct)
        amount_to_be_processed_by_next_processor = amount - actual_notes_to_deduct * 100
        result["100"] = actual_notes_to_deduct
        if amount_to_be_processed_by_next_processor:
            super().withdraw(amount_to_be_processed_by_next_processor, result)
        return result