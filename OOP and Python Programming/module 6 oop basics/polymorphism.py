class animal:
    def __init__(self,name) -> None:
        self.name=name
        
    def make_sound(self):
        print("animal making sound")
    
class cat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
billi=cat("billu")
billi.make_sound()