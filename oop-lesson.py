class Account:
    account_type = ""
    balance = 0
    active = False
    account_number = 000000000
    
    # I've defined a method that takes 2 arguments, an amount to deposit and a string 
    # representing an account_type 
    def deposit(self, amount, account_type):        
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, withdrawal_amount, account_type):
        if withdrawal_amount < self.balance or withdrawal_amount ==self.balance:    #(if) is a conditional test
            self.balance = self.balance - withdrawal_amount
            print('your new balance is {self.balance}')
        else:
            print('insufficient funds, amount requsted is below available balance')
    
    def __init__(self, account_type):
        self.account_type = account_type

A = Account("savings")  # I've created an object called A
# Let's call or access our class Account, using the object we've just created, A.
A.deposit(100, "savings")
A.withdraw(500, "account_type")




print(A.withdraw)
print(A.balance)
print(A.account_type)



    






