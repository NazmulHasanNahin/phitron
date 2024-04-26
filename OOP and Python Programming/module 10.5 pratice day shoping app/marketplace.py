from users import *
class marketplace:
    def __init__(self) -> None:
        self.sellers=[]
        self.customers=[]
        self.products=[]
        
    def register_seller(self,seller):
        self.sellers.append(seller)
    
    def register_customer(self,customer):
        self.customers.append(customer)
        
    def login_user(self,email,password):
        for user in self.customers+self.sellers:
            if user.email == email:
                return user.login_pass_chek(password)
        print("login failed.User not found!!")
        return False
                
    def add_product(self,seller,product):
        if seller in self.sellers:
            seller.add_products(product)
            self.products.append(product)
        else:
            print("Seller is not registered!!!")
        
    def display_products(self):
        available_products=[p for p in self.products if p.stock > 0]
        for product in available_products:
            print(f"product: {product.name}, price: {product.price}, quantity: {product.stock}")
            
    def place_order(self,customer,product,quantity):
        if customer in self.customers:
            ordr=order(customer,product,quantity)
            ordr.process_order()
        else:
            print("customer is not registered!!!")