# 1 Гипотенуза

a = int(input('Введите катет a: ')) # числа целые,положительные, не превышают 1000
b = int(input('Введите катет b: ')) # числа целые,положительные, не превышают 1000

c = ((a*a) + (b*b))**0.5   #c**2 = a**2 + b**2 - теорема пифагора 
print('Гипотенуза =', c)