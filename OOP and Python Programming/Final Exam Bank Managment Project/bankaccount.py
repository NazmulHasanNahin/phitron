import random
class BankAccount:
    def __init__(self,name,email,adress,account_type) -> None:
        self.name=name
        self.email=email
        self.adress=adress
        self.account_type=account_type
        self.balance=0
        self.account_number=random.randint(1000,9999)
        self.transaction_history=[]
        self.loan_taken=0

    def deposit(self,amount):
        self.balance+=amount
        self.transaction_history.append(f"Deposit {amount}")
        print(f"You have deposited {amount} and new balance is {self.balance}")
        
    def withdraw(self,amount):
        if amount >self.balance:
            print("Not enough balance in account!!!")
        else:
            self.balance-=amount
            self.transaction_history.append(f"Withdraw {amount}")
            print(f"You have withdrawed {amount}. New balance is {self.balance}")
            
    def check_balance(self):
        print(f"Available balance: {self.balance}")
    
    def show_transaction(self):
        for transaction in self.transaction_history:
            print(f"{transaction[0]}: {transaction[1]}")
            
    def take_loan(self):
        if self.loan_taken>=2:
            print("You have taken loan 2 time.please pay previous loan money")
        else:
            amount=float(input("Enter loan ammount: "))
            self.loan_taken+=1
            self.deposit(amount)
            print(f"Loan amount {amount} has added.")


