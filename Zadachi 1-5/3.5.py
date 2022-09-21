from math import*
a = float(input('Введите значение a ='))
x = float(input('Введите значение x ='))
if x > 2:
    y=2*a*x-2
    print(f'y = {y:.2f}')
elif x <= 2:
    y=3*a**2-2*x
    print(f'y = {y:2f}')
    
