"""Программа для проверки принадлежности числа к числам Вольстенхольма"""
import math


print('<<<<<<<<<<<<<<<МЕНЮ>>>>>>>>>>>>>>> \n'
      'Введите команду 1: введите число Вольстенхольма \n')


def prost(n):
    """Фунция для проверки числа на простоту
    Входные значения:
        n - целое число
    Выходные значения:
        True - если число простое
        False - иначе"""
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True


if __name__ == "__main__":
    while True:
        p = input()
        if p == 'выход':
            print('вы вышли из программы')
            break
        try:
            p = int(p)
            ch1 = math.factorial(2 * p) // (math.factorial(p) ** 2)
            ch2 = 2
            if prost(p) and abs(ch1 - ch2) % (p ** 4) == 0 and p > 3:
                print(p, '- является числом Вольстенхольма, нечетное')
            else:
                print('не является числом Вольстенхольма')
        except Exception:
            print('введите целое натуральное число')
