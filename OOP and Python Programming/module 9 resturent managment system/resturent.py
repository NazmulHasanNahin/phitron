from menu import menu

class resturent:
    def __init__(self,name) -> None:
        self.name=name    
        self.employees=[]
        self.menu=menu()

    def add_employee(self,employe):
        self.employees.append(employe)
        
        
    def view_employee(self):
        print("---------Employee List---------- ")
        for emp in self.employees:
            print(emp.name,emp.phone,emp.email,emp.adress)