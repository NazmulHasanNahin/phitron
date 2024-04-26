from bankaccount import *


class Bank:
    def __init__(self) -> None:
        self.accounts={}
        self.total_loans=0
        self.loan_system_on=True
        
    def create_account(self, name, email, address, account_type):
        account = BankAccount(name, email, address, account_type)
        self.accounts[account.account_number] = account
        print(f"Account created with number: {account.account_number}")
        
    def delete_account(self,account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted successfully!!!")
        else:
            print("Account does not exist!!!")
        
    def list_account(self):
        for account in self.accounts.values():
            print(f"Account {account.account_number}: {account.name}, {account.account_type}")
    
    def check_total_loans(self):
        print(f"Total Loan: {self.total_loans}")

    def loan_on_off(self):
        self.loan_system_on=not self.loan_system_on
        print("Loan system truned","on" if self.loan_system_on else "off" )  
        
    def transfer_money(self,from_acc,to_acc,amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                print(f"Transfered {amount} from {from_acc} to {to_acc}")
            else:
                print("Insufficient Balance")
        else:
            print("Acoount number does not exist.Try again")
        