# 8 Существует ли треугольник?

a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))

if (a < (b + c)) or (b < (a + c)) or (c < (a + b)) : 
    print ('YES')
else:
    print ('NO')

# Треугольник существует только тогда, когда сумма двух его сторон больше третьей. 
