from users import *
class customer(user):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        
class seller(user):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.products=[]
        
    def add_products(self,product):
        self.products.append(product)
        
class products:
    def __init__(self,name,price,stock) -> None:
        self.name=name
        self.price=price
        self.stock=stock
    
    def update_stock(self,quantity):
        if quantity <= self.stock:
            self.stock-=quantity
        else:
            print("Not enough Stock!!!")