from food_item import food_item
from menu import menu
from users import admin,employee,customer
from resturent import resturent
from orders import order

food_cart=resturent("Food Cart")
def customer_menu():
    name=input("Enter your name: ")
    email=input("Enter your Email: ")
    phone=input("Enter your phone: ")
    adress=input("Enter your adress: ")
    custmer=customer(name=name,phone=phone,email=email,adress=adress)
    
    while True:
        print(f"\nWelcome {custmer.name}\n")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        
        
        choise=int(input("Please enter your option: "))
        if choise==1:
            custmer.view_menu(food_cart)
            
        elif choise == 2:
            item_name=input("Enter item name: ")
            item_quantity=int(input("Enter item quantity: "))
            
            custmer.add_to_cart(food_cart,item_name,item_quantity)
            
        elif choise == 3:
            custmer.view_cart()
            
        elif choise == 4:
            custmer.pay_bill()
            
        elif choise==5:
            break
        
        else:
            print("Invalid Option input")
        
        
    
    
def admin_menu():
    name=input("Enter your name: ")
    email=input("Enter your Email: ")
    phone=input("Enter your phone: ")
    adress=input("Enter your adress: ")
    admn=admin(name=name,phone=phone,email=email,adress=adress)
    
    while True:
        print(f"\nWelcome {admn.name}\n")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")
        
        
        choise=int(input("Please enter your option: "))
        if choise==1:
            item_name=input("Enter item name: ")
            item_quantity=int(input("Enter item quantity: "))
            item_price=int(input("Enter item price: "))
            item=food_item(item_name,item_price,item_quantity)
            admn.add_new_item(food_cart,item)
            
        elif choise == 2:
            name=input("Enter employee name: ")
            email=input("Enter employee email: ")
            phone=input("Enter employee phone: ")
            adress=input("Enter employee adress: ")
            age=input("Enter employee age: ")
            designation=input("Enter employee designation: ")
            salary=input("Enter employee salary: ")
            emplye_detail=employee(name,phone,email,adress,age,designation,salary)
            admn.add_employee(food_cart,emplye_detail)
            
        elif choise == 3:
            admn.view_employee(food_cart)
            
        elif choise == 4:
            admn.view_menu(food_cart)
            
        elif choise==5:
            item_name=input("Enter item name: ")
            admn.remove_item(food_cart,item_name)
            
        elif choise==6:
            break
        
        else:
            print("Invalid Option input")
            
            
            
while True:
    print("Welcome To Food Cart....")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit")
    
    choise=int(input("Enter your choise: "))
     
    if choise == 1:
        customer_menu()
    elif choise == 2:
        admin_menu()
    elif choise == 3:
        break
    else:
        print("Invalid Input")