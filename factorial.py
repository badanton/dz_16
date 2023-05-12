#Factorial через цикл For
# a = int(input('Введите число для вычисления факториала : '))
# b = 1
# for i in range(1,a+1):
#     b *=i
# print(f'Factorial {a} is {b}')


#Factorial через цикл While
# a = int(input('Введите число для вычисления факториала : '))
# b = 1
# while a !=0:
#     b *=a
#     a -=1
# print(f'Factorial {a} is {b}')
#Factorial с помощью модуля math
import math
a = int(input('Введите число для вычисления факториала : '))
print(f'Factorial {a} is {math.factorial(a)}')