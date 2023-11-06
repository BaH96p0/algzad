class Bank():
    def __init__(self, balance, deposit, withdraw, log):
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
        self.log = log

    def dep(self):
        self.balance = self.balance + self.deposit
        self.log = self.log + f'На счет зачислено {self.deposit}. Баланс: {self.balance}\n'

    def wthdrw(self):
        self.balance = self.balance - self.withdraw
        self.log = self.log + f'Со счета снято {self.withdraw}. Баланс: {self.balance}\n'

    def get_log(self):
        return self.log


b = Bank(30000, 5000, 1000, '')
print(b.get_log())
