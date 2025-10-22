from threading import Lock

class Bank:

    def __init__(self, balance: List[int]):
        # 1 - n account numbers
        self.bank = {i+1:balance[i] for i in range(len(balance))}
        #print(self.bank)
        # self.lock = new Lock()

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # money can only be transferred if both accounts exist
        # also only if account1 balance >= money to transfer
        if (account1 in self.bank and account2 in self.bank) and self.bank[account1] >= money:
            self.bank[account1] -= money
            self.bank[account2] += money
            #print(self.bank)
            return True
        #print(self.bank)
        return False

    def deposit(self, account: int, money: int) -> bool:
        # money can only be depo if acct exist
        if account in self.bank:
            self.bank[account] += money
            #print(self.bank)
            return True
        #print(self.bank)
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        # money can only be withdrw if acct exist
        # also only if account balance >= money to withdraw
        #print(self.bank)
        if account in self.bank and self.bank[account] >= money:
            self.bank[account] -= money
            #print(self.bank)
            return True
        #print(self.bank)
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)