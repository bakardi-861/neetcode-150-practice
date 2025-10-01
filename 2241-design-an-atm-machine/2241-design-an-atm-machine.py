class ATM:
    # bills: 5,20,50,100,200,500

    def __init__(self):
        self.values = [20, 50, 100, 200, 500]
        self.counts = [0] * 5
        

    def deposit(self, banknotesCount: List[int]) -> None:
        # $20, $50, $100, $200, and $500.
        for i,billCount in enumerate(banknotesCount):
            self.counts[i] += billCount

    def withdraw(self, amount: int) -> List[int]:
        # prioritize larger bill types when withdrawing: convert to largest possible first
        # if amount > sum of bill types ($600 and there are 3 $200 bills and 1 $500 bills), it is impossible because 500 + 200 > 600
        # machine can't use the 200 bills instead because it has to use larger bills first

        # self.atm = {0:[20,0],1:[50,0],2:[100,1],3:[200,2],4:[500,1]}
        # [0,0,1,0,1]
        # amount = 0
        # largest = 500
        # i = 2

        # iterate by largest bill
        counts_backup = [self.counts[i] for i in range(5)]
        atm_bills = [0] * 5
        for i in reversed(range(5)):
            max_usable_bills = min(amount // self.values[i], self.counts[i])
            if max_usable_bills:
                atm_bills[i] += max_usable_bills
                amount -= (self.values[i] * max_usable_bills)
                self.counts[i] -= max_usable_bills

        if amount:
            self.counts = counts_backup
            return [-1]
        else:
            return atm_bills            
            




# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)