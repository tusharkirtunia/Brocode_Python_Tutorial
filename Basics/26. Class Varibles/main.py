# Class Variables = Shared among all instances of a class
#                   Defined outside the constructor 
#                   Allow you to share data among all object created from that class

class Student:
    
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Tushar", 20)
student2 = Student("Dilip", 45)
student3 = Student("Sandhya", 42)
student4 = Student("Naresh", 90)

#print (student2.name)
#print (student2.age)
#print (student1.class_year)

print (f"My graduating class of {Student.class_year} has {Student.num_students} students")
print (student1.name)
print (student2.name)