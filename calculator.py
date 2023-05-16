# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

class Calculator:

    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def symma(self):
        """Сумма"""
        print(self.a + self.b)

    def razn(self):
        """Разность"""
        print(self.a - self.b)

    def umnoj(self):
        """Умножение"""
        print(self.a * self.b)

    def delen(self):
        """Деление"""
        print(self.a / self.b)

    def vvod(self):
        self.a = int(input('Enter the first number : '))
        self.b = int(input('Enter the second number : '))
        self.c = input('Enter a mathematical action : ')


obj = Calculator()

while True:
    try:
        # obj = Calculator(a=int(input('Enter the first number : ')), b=int(input('Enter the second number : ')),
        #                  c=input('Enter a mathematical action : '))
        obj.vvod()
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
        else:
            print('Некоректный ввод')
    except ZeroDivisionError:
        print('Деление на 0')
    except Exception:
        print('Некоректный ввод')
