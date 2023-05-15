#  Factorial через цикл For

# a = int(input('Введите число для вычисления факториала : '))
# b = 1
# for i in range(1,a+1):
#     b *=i
# print(f'Factorial {a} is {b}')


#  Factorial через цикл While
# a = int(input('Введите число для вычисления факториала : '))
# b = 1
# while a !=0:
#     b *=a
#     a -=1
# print(f'Factorial {a} is {b}')
#  Factorial с помощью модуля math
# import math
# a = int(input('Введите число для вычисления факториала : '))
# print(f'Factorial {a} is {math.factorial(a)}')

# Illustration of creating a class
# in Python with input from the user
class Student:
    'A student class'
    stuCount = 0

    # initialization or constructor method of
    def __init__(self):
        # class Student
        self.name = input('enter student name:')
        self.rollno = input('enter student rollno:')
        Student.stuCount += 1

    # displayStudent method of class Student
    def displayStudent(self):
        print("Name:", self.name, "Rollno:", self.rollno)


stu1 = Student()
stu2 = Student()
stu3 = Student()
stu1.displayStudent()
stu2.displayStudent()
stu3.displayStudent()
print('total no. of students:', Student.stuCount)
