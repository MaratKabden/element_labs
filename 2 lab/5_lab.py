# 5 Перевод числа

import math
x = (input('Введите x в двоичной системе: ')) # в двоичном числе не более 10 цифр

a = 0
b = 0
 
for i in reversed(range(0, len(x))):
    a += (int(x[i]) * int(math.pow(2, b)))
    b += 1
 
print ('Введенный x в десятичной системе:', a)