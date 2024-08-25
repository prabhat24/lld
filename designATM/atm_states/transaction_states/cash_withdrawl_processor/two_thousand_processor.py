from abc import ABC, abstractmethod

from .withdrawl_processor import WithdrawlProcessor

class TwoThousandWithdrawlProcessor(WithdrawlProcessor):

    def withdraw(self, amount, result):
        two_thousand_notes_to_deduct = 0
        max_two_thousand_notes_to_deduct = amount // 2000
        two_thousand_notes_to_deduct = min(self.atm.get_two_thousand_notes(), max_two_thousand_notes_to_deduct)
        amount_to_be_processed_by_next_processor = amount - two_thousand_notes_to_deduct * 2000
        result["2000"] = two_thousand_notes_to_deduct
        if amount_to_be_processed_by_next_processor:
            super().withdraw(amount_to_be_processed_by_next_processor, result)
        return result