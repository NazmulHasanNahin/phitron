# from school import school
# from classroom import classroom
# from subject import subject
# from person import student,teacher


# scl=school("gai","Dhaka")

# #adding classroom
# eight=classroom("Eight")
# nine=classroom("Nine")
# ten=classroom("Ten")

# scl.add_classroom(eight)
# scl.add_classroom(nine)
# scl.add_classroom(ten)


# #adding student

# rahim=student("rahim",eight)
# karim=student("karim",nine)
# fahim=student("fahim",ten)
# hamim=student("hamim",ten)

# school.student_addmission(scl,rahim)
# school.student_addmission(scl,karim)
# school.student_addmission(scl,fahim)
# school.student_addmission(scl,hamim)

# # adding teacher

# abul=teacher("abul")
# babul=teacher("babul")
# kabul=teacher("kabul")

# # adding subject

# bangla=subject("bangla",abul)
# english=subject("english",babul)
# math=subject("math",kabul)


# eight.add_subject(bangla)
# eight.add_subject(english)
# eight.add_subject(math)
# nine.add_subject(bangla)
# nine.add_subject(english)
# nine.add_subject(math)
# ten.add_subject(bangla)
# ten.add_subject(english)
# ten.add_subject(math)

# #take final exam 

# eight.take_semester_final_exam()
# # print(scl)




from school import school
from person import student, teacher
from subject import subject
from classroom import classroom

college = school("ABC", "Dhaka")

# Adding Classroom
eight = classroom("Eight")
nine = classroom("Nine")
ten = classroom("Ten")

college.add_classroom(eight)
college.add_classroom(nine)
college.add_classroom(ten)

# Adding Student
rahim = student("Rahim", eight)
karim = student("Karim", nine)
fahim = student("Fahim", ten)
hamim = student("Hamim", ten)

college.student_addmission(rahim)
college.student_addmission(karim)
college.student_addmission(fahim)
college.student_addmission(hamim)

# Adding Teachers
abul = teacher("Abul Khan")
babul = teacher("Babul Khan")
kabul = teacher("Kabul Khan")

# Adding Subjects
bangla = subject("Bangla", abul)
physics = subject("Physics", babul)
chemistry = subject("Chemistry", kabul)
biology = subject("Biology", kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(college)