import math


def prost(n):  # проверка простое число или нет
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True


while True:
    p = input()  # вводим
    if p == 'выход':
        print('вы вышли из программы')
        break
    try:  # обработка ошибок
        p = int(p)
        ch1 = math.factorial(2 * p) // (math.factorial(p) ** 2)  # число слева
        ch2 = 2  # число справа
        if prost(p) and abs(ch1 - ch2) % (p ** 4) == 0 and p > 3:  # сравнение по модулю
            print(p, '- является числом Вольстенхольма, нечетное')
        else:
            print('не является числом Вольстенхольма')
    except Exception:
        print('введите целое натуральное число')
