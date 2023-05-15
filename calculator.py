# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

class Calculator:
    def __init__(self, a, b, c):  # динамические свойства
        self.a = a
        self.b = b
        self.c = c

    def symma(self):
        '''Сумма'''
        print(self.a + self.b)

    def razn(self):
        '''Разность'''
        print(self.a - self.b)

    def umnoj(self):
        '''Умножение'''
        print(self.a * self.b)

    def delen(self):
        '''Деление'''
        print(self.a / self.b)

    # def vvod(self):
    #     self.a = int(input('Enter the first number : '))
    #     self.c = input('Enter a mathematical action : ')
    #     self.b = int(input('Enter the second number : '))


while True:
    try:
        obj = Calculator(a=int(input('Enter the first number : ')), b=int(input('Enter the second number : ')),
                         c=input('Enter a mathematical action : '))

        if obj.c == '0':
            break
        if obj.c == '+':
            obj.symma()
        elif obj.c == '-':
            obj.razn()
        elif obj.c == '*':
            obj.umnoj()
        elif obj.c == '/':
            obj.delen()
    except ZeroDivisionError:
        print('Деление на 0')
