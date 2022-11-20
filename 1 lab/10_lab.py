# 10 Упорядочить три числа

a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))

if a >= b and a >= c and b >= c:
    print(c, b, a)
elif b >= a and b >= c and a >= c:
    print(c, a, b)
elif c >= a and c >= b and a >= b:
    print(b, a, c)
elif a >= b and a >= c and c >= b:
    print(b, c, a)
elif b >= a and b >= c and c >= a:
    print(a, c, b)
else:
    print(a, b, c)