n = 0
a = int(input('Введите a: '))
b = int(input('Введите b: '))

def square(a, b, n):

    if a == b:
        return a, b, n

    elif a < b:
        print('Отрезали квадрат: ', a, b)
        return square(a, b-a, n+1)

    else:
        print('Отрезали квадрат: ', b, a)
        return square(a-b, b, n+1)

print('Размер последнего квадрата и  количество полученных квадратов: ', square(a, b, n))


