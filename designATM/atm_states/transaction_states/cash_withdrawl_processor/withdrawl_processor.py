class WithdrawlProcessor():

    def __init__(self, atm, next_processor):
        self.next_processor = next_processor
        self.atm = atm


    def withdraw(self, amount, result):
        if self.next_processor != None:
            return self.next_processor.withdraw(amount, result)
        else:
            print("withdrawl request could not be processed")
            print(self.atm.get_state())
            self.atm.get_state().exit()