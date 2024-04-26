from bankaccount import *
from bank import *


def user_interface(bank):
    while True:
        print("\nUser Interface\n")
        print("1.Create Account")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Check Balance")
        print("5.Transaction History")
        print("6.Take Loan")
        print("7.Transfer Money")
        print("8.Exit")
        
        choice = int(input("Choose an option: "))
        if choice ==1:
            name=input("Enter your name: ")
            email=input("Enter your mail: ")
            address=input("Enter your address: ")
            account_type=input("Enter your account type(Savings/current): ")
            bank.create_account(name, email, address, account_type)
        
        elif choice ==2:
            acc_num = int(input("Enter your account number: "))
            if acc_num in bank.accounts:
                amount=float(input("Enter amount to deposit: "))
                bank.accounts[acc_num].deposit(amount)
            else:
                print("Account does not exist.")
                                
        elif choice ==3:
            acc_num = int(input("Enter your account number: "))
            if acc_num in bank.accounts:
                amount=float(input("Enter amount to withdraw: "))
                bank.accounts[acc_num].withdraw(amount)
            else:
                print("Account does not exist.")
                
        elif choice ==4:
            acc_num = int(input("Enter your account number: "))
            if acc_num in bank.accounts:
                bank.accounts[acc_num].check_balance()
            else:
                print("Account does not exist.")
                
        elif choice ==5:
            acc_num = int(input("Enter your account number: "))
            if acc_num in bank.accounts:
                bank.accounts[acc_num].show_transactions()
            else:
                print("Account does not exist.")
                
        elif choice ==6:
            acc_num = int(input("Enter your account number: "))
            if acc_num in bank.accounts:
                if bank.loan_system_on:
                    bank.accounts[acc_num].take_loan()
            else:
                print("Account does not exist.")
                
        elif choice ==7:
            acc_num = int(input("Enter your account number: "))
            to_acc = int(input("Enter destination account number: "))
            amount = float(input("Enter amount to transfer: "))
            if acc_num in bank.accounts:
                bank.transfer_money(acc_num, to_acc, amount)
            else:
                print("Account does not exist.")
        elif choice ==8:
            break
        else:
            print("Invalid Option!!!")

def admin_interface(bank):
    while True:
        print("\nAdmin Interface\n")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. List All Accounts")
        print("4. Total Balance")
        print("5. Total Loans")
        print("6. Toggle Loan Feature")
        
        admin_choice=int(input("Enter option: "))
        if admin_choice == 1:
            name = input("Enter admin name: ")
            email = input("Enter admin email: ")
            address = input("Enter admin address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif admin_choice == 2:
            acc_num = int(input("Enter account number to delete: "))
            if acc_num in bank.accounts:
                bank.delete_account(acc_num)
            else:
                print("Account does not exist.")
        elif admin_choice == 3:
            bank.list_account()
        elif admin_choice == 4:
            bank.total_balance()
        elif admin_choice == 5:
            bank.check_total_loans()
        elif admin_choice == 6:
            bank.loan_system_on = not bank.loan_system_on
            print("Loan system toggled ", "on" if bank.loan_system_on else "off")
        elif admin_choice==7:
            break
        else:
            print("Invalid option. Please try again.")
            

          
bank=Bank()                
while True:
    print("\nWelcome to the BANK")
    print("\n1.User")
    print("2.Admin")
    print("3.Exit")
    choice = int(input("Choose an option: "))
    if choice ==1:
        user_interface(bank)
    elif choice==2:
        admin_interface(bank)  
    elif choice ==3:
        break
    else:
        print("Invalid option") 