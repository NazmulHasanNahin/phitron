class person:
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def __add__(self,others):
        return self.age + others.age
    
class crickter(person):
    def __init__(self, name, age, height, weight,team) -> None:
        super().__init__(name, age, height, weight)
        self.team=team
       #override 
    def eat(self):
        print("diet plan for players")
        
sakib=crickter("sakib",34,5.8,60,"bangladesh")

mushfiq=crickter("mush",34,5,5.5,"bangladesh")
sakib.eat()
print(sakib + mushfiq)