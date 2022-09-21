#Напечатать квадраты всех целых чисел от A до B ( A < B ) с шагом H
A = int(input())
B = int(input())
H = int(input())
if A >= B:
    print('False')
else:
    while A <= B:
        C = A**2
        print(C)
        A = A+H
        if A>B:
            break
