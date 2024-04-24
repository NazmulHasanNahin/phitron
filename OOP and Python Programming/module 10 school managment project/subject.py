from school import school
from person import teacher
class subject:
    def __init__(self,name,teacher) -> None:
        self.name=name
        self.teacher=teacher
        self.max_marks=100
        self.pass_marks=33
    
    
    def exam(self,students):
        for student in students:
            mark=self.teacher.evalaute_exam()
            student.marks[self.name]=mark
            student.subject_grade[self.name]=school.calculate_grade(mark)