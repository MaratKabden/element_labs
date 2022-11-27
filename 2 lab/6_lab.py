# 6 Степень

def pow_(a, n):
    if(n == 0):
        return 1
    elif(n == 1):
        return a
    else:
        res = float(a)
        for i in range(2, n+1):
            res *= a
        return res

a = input('Введите два числа: ').split()

print(pow(float(a[0]), int(a[1])))