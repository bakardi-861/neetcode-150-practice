class Bank:

    def __init__(self, balance: List[int]):
        self.bank = {i+1:balance[i] for i in range(len(balance))}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # either account is not in bank or money > account1 balance, False
        if not account1 in self.bank or not account2 in self.bank or money > self.bank[account1]:
            return False

        self.bank[account1] -= money
        self.bank[account2] += money
        return True


    def deposit(self, account: int, money: int) -> bool:
        if account not in self.bank:
            return False

        self.bank[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.bank or money > self.bank[account]:
            return False
        
        self.bank[account] -= money
        return True

    # top k
        
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)