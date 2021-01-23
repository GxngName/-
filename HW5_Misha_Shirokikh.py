def ds():
     max = 0
     num = int(input("Введите число: "))
     while num > 0:
         rest = num % 2
         if max < rest:
             max = rest
             if (max == 0):
                break
        num = num // 10
        print(num)
     return max

max = ds()
print(max)


import math
print("Значения ax^2+bx+c=0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def discriminant (a, b, c):
    discriminant = b**2 - 4*a*c
    if  discriminant >= 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print('x₁ = ' + str(x1))
        print('x₂ = ' + str(x2))
    if discriminant <= 0:
         print('Корней нет')

f = discriminant(a,b,c)
print(f)