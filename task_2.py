class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
       
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
       
        
  

class Revewier(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
   def __init__(self, name, surname):
       super().__init__(name, surname)
       self.courses_in_progress = []
       self.grades = {}


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_revewie = Revewier('Some', 'Buddy')
cool_revewie.courses_attached += ['Python']
 
cool_revewie.rate_hw(best_student, 'Python', 10)
cool_revewie.rate_hw(best_student, 'Python', 10)
cool_revewie.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)



cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_in_progress += ['Python, Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_attached += ['Python, Git']
 
best_student.rate_lw(cool_lecturer, 'Python, Git', 9)
best_student.rate_lw(cool_lecturer, 'Python, Git', 8)
best_student.rate_lw(cool_lecturer, 'Python, Git', 10)
 
print(cool_lecturer.grades)