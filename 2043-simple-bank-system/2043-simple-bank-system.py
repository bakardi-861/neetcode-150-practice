class Bank:

    def __init__(self, balance: List[int]):
        self.bank = balance
        self.n = len(balance)
        # 0 to n-1 accounts

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # either account doesnt exist or money > account1 balance
        if self.n < account1-1 or self.n < account2-1 or money > self.bank[account1-1]:
            return False
        self.bank[account1-1] -= money
        self.bank[account2-1] += money
        return True


    def deposit(self, account: int, money: int) -> bool:
        if self.n < account-1:
            return False
        self.bank[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if self.n < account-1 or money > self.bank[account-1]:
            return False
        self.bank[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)