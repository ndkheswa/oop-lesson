class Account:
    account_type = ""
    balance = 0
    active = False
    account_number = 000000000

    def deposit(self, amount, account_type):
        self.balance = self.balance + amount
        return self.balance
        
    def withdraw(self, withdrawal_amount, account_type):
        if withdrawal_amount < self.balance or withdrawal_amount == self.balance:
            self.balance = self.balance - withdrawal_amount
            print(f'Your new balance is {self.balance}')
        else:
            print('Insufficient funds, amount requested is below available balance')

A = Account ()


A.deposit(500, 'cheque')
print(f'{A.balance}')

A.withdraw(150, 'checque')



            


