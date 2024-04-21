class vehicle:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
    
    def move(self):
        pass
    
class bus(vehicle):
    def __init__(self, name, price,seat) -> None:
        super().__init__(name, price)
        self.seat=seat
        
class truck(vehicle):
    def __init__(self, name, price,weight) -> None:
        super().__init__(name, price)
        self.weight=weight
        
class pickup(truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)
        
        
class acbus(bus):
    def __init__(self, name, price, seat,tmp) -> None:
        super().__init__(name, price, seat)
        self.tmp=tmp
        
        
green_line=acbus("hanif",34342,"buisness_class","normal")
        
        