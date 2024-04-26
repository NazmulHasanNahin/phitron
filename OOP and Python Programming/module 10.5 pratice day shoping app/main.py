from customer import *
from marketplace import * 
from users import *

market=marketplace()

def handle_customer(market):
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    
    cust=customer(email,password)
    market.register_customer(cust)
    
    while True:
        print("\nCustomer Menu\n")
        print("1.Display Order")
        print("2.Place order")
        print("3.Back to main menu")
    
        choise=int(input("Please select an option: "))
        if choise == 1:
            market.display_products()
        elif choise == 2:
            place_order(cust,market)
        elif choise==3:
            break
        else:
            print("Invalid Option!!!")
        
def place_order(cust,market):
    product_name = input("Enter the name of the product you want to buy: ")
    quantity = int(input("Enter the quantity: "))
    
    product=product = next((p for p in market.products if p.name == product_name and p.stock > 0), None)        
    if product:
        market.place_order(cust,product,quantity)
    else:
        print("Product stock out or not available!!")   


        
    
def handle_seller(market):
    email=input("Enter your email: ")
    password=input("Enter your password: ") 
    
    sellr=seller(email,password)
    market.register_seller(sellr)
    
    while True:
        print("\nSeller Menu\n")
        print("1.Add product")
        print("2.display product")
        print("3.back to main menu")
        
        
        choise=int(input("Please select an option: "))
        if choise==1:
            add_product(sellr,market)
        elif choise==2:
            market.display_products()
        elif choise==3:
            break
        else:
            print("Invalid Option!!!")
            

def add_product(sellr,market):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))

    product = products(name, price, stock)
    sellr.add_products(product)
    market.add_product(sellr, product)
    print("Product added successfully.")

       
    
while True:
    print("\nWelcome to Goribs Shopping App!!")
    print("1.Customer")
    print("2.Seller")
    print("3.Exit")
     
    choise=int(input("Please select an option: "))
    if choise==1:
        handle_customer(market)
    elif choise==2:
        handle_seller(market)
    elif choise==3:
        break
    else:
        print("Invalid Option!!!")
    
    