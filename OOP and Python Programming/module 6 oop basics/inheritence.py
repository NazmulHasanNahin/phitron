class gadget:
    def __init__(self,brand,price,color,origin):
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin
        
class laptop:
    def __init__(self,memory):
        self.memory=memory
    def run(self):
        return f"running laptop :{self.brand}"
    def coding(self):
        return f"learning python with phitron.io"


class phone(gadget):
    def __init__(self,brand,price,color,origin,dual_sim):
        self.dual_sim=dual_sim
        super().__init__(brand,price,color,origin)
    
        
    def run(self):
        return f"running phone :{self.brand}"
    
    def phone_call(self,num,text):
        return f"sending sms to {num} with {text}"
    
    def __repr__(self) -> str:
        return f"dual sim supported : {self.dual_sim}"
  
class camera:
    def __init__(self,pixel):
        self.pixel=pixel
        
    def run(self):
        pass
    def lens(self):
        pass
    
    
# inheritence

my_phn=phone("realme",36000,"gray","china",True)

print(my_phn)

    
    