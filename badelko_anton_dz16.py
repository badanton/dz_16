# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def symma(a, b):
    '''Сумма'''
    return a + b
def razn(a, b):
    '''Разность'''
    return a - b
def umnoj(a, b):
    '''Умножение'''
    return a * b
def delen(a, b):
    '''Деление'''
    return a / b
while True:
    try:
        a = int(input('Введите a: '))
        c = input('Введите операцию + - / * 0-выход: ')
        if c == '0':
            break
        b = int(input('Введите b: '))
        if c == '+':
            print(symma(a, b))
        elif c == '-':
            print(razn(a, b))
        elif c == '*':
            print(umnoj(a, b))
        elif c == '/':
            print(delen(a, b))
    except ZeroDivisionError:
        print('Деление на 0')


