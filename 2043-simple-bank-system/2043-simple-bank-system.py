class Bank:
    # valid transaction
    # 1. account number is from 1 to n (len(balance))
    # 2. the amount of money withdrawn/transferred <= account balance

    # Time: O(n) for creating accounts map and O(1) for everything else
    # Space: O(n) store the accounts

    def __init__(self, balance: List[int]):
        # create hashmap of accounts and insert balances as {i:balance[i]}
        # if i already in accounts, don't insert anything
        self.balance = balance
        self.n = len(balance)
        #print(self.accounts)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # if either account is not in accounts, return False.
        if account1-1 > self.n or account2-1 > self.n or money > self.balance[account1-1]:
            return False
        
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        #print(self.accounts)
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        self.balance[account-1] += money
        #print(self.accounts)
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n or money > self.balance[account-1]:
            return False
        self.balance[account-1] -= money
        #print(self.accounts)
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)