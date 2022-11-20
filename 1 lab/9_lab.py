# 9 Количество равных из трех

a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)