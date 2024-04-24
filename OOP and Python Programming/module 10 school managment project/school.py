class school:
    def __init__(self,name,adress) -> None:
        self.name=name
        self.adress=adress
        self.teachers={}
        self.classrooms={}
        
    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom
        
    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher
        
    def student_addmission(self,student):
        classname=student.classroom.name
        self.classrooms[classname].add_student(student)
    
    @staticmethod
    
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return "A+"
        elif marks >=70 and marks<=79:
            return "A"
        elif marks >=60 and marks<=69:
            return "A-"
        elif marks >=50 and marks<=59:
            return "B"
        elif marks >=40 and marks<=49:
            return "C"
        elif marks >=33 and marks<=39:
            return "D"
        else:
            return "F"
        
    
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            "A+" : 5.00,
            "A" : 4.50,
            "A-" : 4.00,
            "B" : 3.50,
            "C" : 3.00,
            "D" : 2.50,
            "F" : 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value>=4.50 and value <=5.00:
            return "A+"
        elif value >=3.50 and value <4.50:
            return "A"
        elif value>=3.00 and value < 3.5:
            return "A-"
        elif value >= 2.5 and value <3.0:
            return "B"
        elif value >=2.0 and value <2.5:
            return "C"
        elif value >=1.0 and value < 2.0:
            return "D"
        else:
            return "F"
        
    def __repr__(self):
        #all classroom 
        for key in self.classrooms.keys():
            print(key)
        # all student 
        print("All Student")
        result=""
        for key,value in self.classrooms.items():
            result+=f"----{key.upper()} Classroom Students\n"
            for student in value.students:
                result+=f"{student.name}\n"
        print(result)
         
        # all subject
        subject=""
        for key,value in self.classrooms.items():
            subject+=f"----{key.upper()} Classroom subjects\n"
            for sub in value.subjects:
                subject+=f"{sub.name}\n"
        print(subject)
        
        # all teacher
         
        # all student result
        print("students results")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.calculate_final_grade())        
        return ""
        
        
        