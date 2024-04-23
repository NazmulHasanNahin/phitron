# customer 
# employe 
# admin
# user of the system
from orders import order
from abc import ABC

class user(ABC):
    def __init__(self,name,phone,email,adress) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.adress=adress
        
        
class customer(user):
    def __init__(self, name, phone, email, adress) -> None:
        super().__init__(name, phone, email, adress)
        self.cart=order()
        
    def view_menu(self,resturent):
        resturent.menu.show_menu()
        
    def add_to_cart(self,resturent,item_name,quantity):
        item=resturent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("Item not found.")
        
    def view_cart(self):
        print("-----Your Cart------")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")
      
    def pay_bill(self):
          print(f"Total {self.cart.total_price} paid successfully")
          self.cart.clear()
      
    
class employee(user):
    def __init__(self, name, phone, email, adress,age,designation,salary) -> None:
        super().__init__(name, phone, email, adress)
        self.age=age
        self.designation=designation
        self.salary=salary
        
        
class admin(user):
    def __init__(self, name, phone, email, adress) -> None:
        super().__init__(name, phone, email, adress)
        
        
    def add_employee(self,resturent,employee):
        resturent.add_employee(employee)

        
    def view_employee(self,resturent):
        resturent.view_employee()
        
    def add_new_item(self,resturent,item):
        resturent.menu.add_menu_item(item)
        
    def remove_item(self,resturent,item):
        resturent.menu.remove_item(item)
           
    def view_menu(self,resturent):
        resturent.menu.show_menu()
    
    
# ad=admin("nahin",1234,"n@gmail.com","dhaka")
# ad.add_employees("nisad","nisad@gmail.com",12334,"dhaka",13,"cook",10000)
# ad.view_employee()        

# doakan=resturent("dokan")
# mn=menu()
# itm1=food_item("drinks",100,20)
# itm2=food_item("burger",130,50)
# admin1=admin("nahinADMIN",436532,"admin@gmai;.com","dhaka")

# admin1.add_new_item(doakan,itm1)
# admin1.add_new_item(doakan,itm2)
# # mn.show_menu()
# customer1=customer("nahin",2134,"nahin@gmai;.com","dhaka")
# customer1.view_menu(doakan)

# item_name=input("Enter item name: ")
# item_quantity = int(input("Enter the quantity: "))

# customer1.add_to_cart(doakan,item_name,item_quantity)
# customer1.view_cart()
