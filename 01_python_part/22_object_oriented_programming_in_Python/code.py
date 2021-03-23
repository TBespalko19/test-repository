# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


# def average(sequence):
#     return sum(sequence) / len(sequence)


# print(average(student["grades"]))

# # But wouldn't it be nice if we could...
# # print(student.average()) $ AttributeError: 'dict' object has no attribute 'average'


# -- Parameters in __init__ --

# class Student:
#     def __init__(self): # convension
#         self.name = "Rolf"
#         self.grades = (90, 90, 93, 78, 90)

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)

# student = Student() # creates new empty container and it runs the init method (method not function - because inside of the class)
# # print(student.name)
# # print(student.grades)
# # average(student.grades) # NameError: name 'average' is not defined

# ## OOP -you call a class, the init method runs (and you get the new object placed in studebnt) and what you get back is the object you created and in the init method you have the opportunity
# ## to set and change its propertied

# print(Student.average_grade(student)) ## The Class then call another function you put in therer the student object
# ## hauling the average method inside that's what the dot means (inside a Student Class) and the self parameter is going to take the value
# ## of the student variable which has that object that was created earlier on that contains

# ## self.name = "Rolf"
# ## self.grades = (89, 90, 93, 78, 90)


# # -- *args 

# print(student.average_grade())


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student1 = Student("Rolf", (89, 90, 93, 78, 90))
student2 = Student("Bob", (36, 67, 90, 100, 100))
print(student1.average_grade())
print(student2.average_grade())


## with *args
class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student1 = Student("Rolf", 89, 90, 93, 78, 90)
student2 = Student("Bob", 36, 67, 90, 100, 100)
print(student1.average_grade())
print(student2.average_grade())
