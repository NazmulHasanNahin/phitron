import random
from school import school
class person:
    def __init__(self,name) -> None:
        self.name=name
        
        
class teacher(person):
    def __init__(self, name) -> None:
        super().__init__(name)
        
        
    def evalaute_exam(self):
        return random.randint(1,100)
    

class student(person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom=classroom
        self.__id=None
        self.marks={}
        self.subject_grade={}
        self.grade =None
        
        
    def calculate_final_grade(self):
        sum=0
        for grade in self.subject_grade.values():
            point=school.grade_to_value(grade)
            sum+=point
        if sum==0:
            gpa=0.00
            self.grade="F"
        else:
            gpa=sum/len(self.subject_grade)
            self.grade=school.value_to_grade(gpa)
        return f"{self.name} final grade : {self.grade} with gpa = {gpa}"
        
       
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id=value
