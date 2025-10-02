class Bank:
    # n counts: 1 - n
    # balance for each account is stored in a 0-index array
    # account "i+1" = balance[i]

    # Valid:
    # 1: account numbers are between 1 - n
    # 2: money withdrawn/transferred is <= balance[i]

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        b = self.balance
        # if account numbers are valid
        if 1 <= account1 <= len(b) and 1 <= account2 <= len(b):
            # account1 -> account2, check account1-1 balance
            if money <= b[account1-1]:
                b[account2-1] += money
                b[account1-1] -= money
                return True
        return False


    def deposit(self, account: int, money: int) -> bool:
        b = self.balance
        if 1 <= account <= len(b):
            b[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        b = self.balance
        if 1 <= account <= len(b) and money <= b[account-1]:
            b[account-1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)