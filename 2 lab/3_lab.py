# 3 Делители числа

x = int(input('Введите целое число: '))   

for i in range (1, x+1): 
    if x % i == 0:
        print(i, end=' ')

