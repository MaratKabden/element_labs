# 2 Минимальный делитель

x = int(input('Введите целое число: '))   # a <= b

# 2 <= x <= 30000

for i in range(2, x+1):
    if not x % i:
        print(i)
        break