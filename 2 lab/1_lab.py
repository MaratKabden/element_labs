# 1 Четные числа

a = int(input('Введите целое число: '))   # a <= b
b = int(input('Введите целое число: '))   

for i in range (a, b+1):
    if i % 2 == 0:
        print(i, end=' ')