class company:
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress
        self.bus=[]
        self.routes=[]
        self.driver=[]
        self.manager=[]
        self.supervisor=[]
        self.fare=[]

class driver:
    def __init__(self,name,licence,age):
        self.name=name
        self.licence=licence
        self.age=age
        
class counter:
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self,start,end):
        pass
    

class passenger:
    pass


class supervisor:
    pass

lal_mia=driver("lal mia",111,37)
