class Bank:
    # valid transaction
    # 1. account number is from 1 to n (len(balance))
    # 2. the amount of money withdrawn/transferred <= account balance

    def __init__(self, balance: List[int]):
        # create hashmap of accounts and insert balances as {i:balance[i]}
        # if i already in accounts, don't insert anything
        self.accounts = {}
        for i in range(len(balance)):
            if i+1 not in self.accounts:
                self.accounts[i+1] = balance[i]
        #print(self.accounts)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # if either account is not in accounts, return False.
        if account1 not in self.accounts or account2 not in self.accounts or money > self.accounts[account1]:
            return False
        
        self.accounts[account1] -= money
        self.accounts[account2] += money
        #print(self.accounts)
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.accounts:
            return False
        self.accounts[account] += money
        #print(self.accounts)
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.accounts or money > self.accounts[account]:
            return False
        self.accounts[account] -= money
        #print(self.accounts)
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)