class laptop:
    def __init__(self,brand,price,color,memory):
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
    def run(self):
        return f"running laptop :{self.brand}"
    def coding(self):
        return f"learning python with phitron.io"


class phone:
    def __init__(self,brand,price,color,dual_sim):
        self.brand=brand
        self.price=price
        self.color=color
        self.dual_sim=dual_sim
        
    def run(self):
        return f"running phone :{self.brand}"
    
    def phone_call(self,num,text):
        return f"sending sms to {num} with {text}"
    
    
    
class camera:
    def __init__(self,brand,price,color,pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel
        
    def run(self):
        pass
    def lens(self):
        pass
    
    
    
    
    