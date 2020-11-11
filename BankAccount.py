import random #import to have random number for account_number
num = range(10000000, 99999999)
class BankAccount():
    routing_number = 111111111 #attibute unchanged
    def __init__(self, full_name): #instance variable subject to change / different per person
        self.full_name = full_name
        self.account_number = random.choice(num)
        self.balance = 0
    #end init
    def deposit(self, amount):
        self.balance += amount
        return print(f"Amount Deposited: ${amount}")
    #end deposit
    def withdraw(self, amount):
        if self.balance >= amount: #checks 
            self.balance -= amount
            return print(f"Amount Withdrawn: ${amount}")
        else:
            self.balance -= (amount + 10.00)
            return print("Insufficent Funds.")
    #end withdraw()
    def get_balance(self):
        print(f"Your current balance is: {self.balance}")
        return self.balance
    #end get_balance
    def add_interest(self):
        interest = self.balance *  0.00083 
        self.balance += interest
    #end add_interest
    def print_receipt(self):
        print(self.full_name)
        print(f"Account No.:{self.account_number}")
        print(f"Routing No.:{self.routing_number}")
        print(f"Balance: ${self.balance}")
    #end print_receipt
#end class bankaccount

t1 = BankAccount("Christopher De La Torre")
t2 = BankAccount("Ricky Picky")
t3 = BankAccount("Bob Builder")

t1.deposit(500)
t1.get_balance()
t1.withdraw(500)
t2.deposit(1000)
t2.add_interest()
t2.print_receipt()
t3.withdraw(500)
t3.get_balance()

