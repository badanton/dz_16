# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.

def proverka(a):
    b = 0  # сумма длинн слов в кортеже
    c = 0  # кол-во цифр в списке
    d = 0  # кол-во букв в списке
    g = 0  # кол-во не четных цифр
    h = 0  # кол-во букв в строке
    if type(a) is tuple:
        for i in a:
            if type(i) is str:
               # print(i, '-', len(i))
                b += len(i)
        print(f'1.Сумма длинн всех слов в кортеже {a} равна {b}.')
    elif type(a) is list:
        a1 = a
        a = [str(j) for j in a]
        a = ''.join(a)
        for k in a:
            if k.isdigit():
                c += 1
            elif k.isalpha():
                d += 1
        print(f'2. Список {a1} содержит {c} цифр и {d} букв.')
    elif type(a) is int:
        a = str(a)
        for i in a:
            if int(i) % 2 != 0:
                g += 1
        print(f'3. Число {a} содержит {g} нечетных цифр.')
    elif type(a) is str:
        for n in a:
            if n.isalpha():
                h += 1
        print(f'4. Строка {a} содержит {h} букв.')


proverka(('afafaf', ['13', '141'], 'sdfnk', 'fsdfksmkf', 'sdlfnflslnf'))
proverka([234, 2, 35435, 45426, 'adf14', 2, 'sfdssff', '1414rewwe'])
proverka(124314144134412133)
proverka('12431/.shsh4 1441gsdfsg/dfh3441sd? hfsdfh2133')
