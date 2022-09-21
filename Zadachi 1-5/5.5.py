import random
n = random.randint(1,15)
c = 0

for i in range(1,n+1):
    c+=i**3
    c-=(i+1)**3
c
print(c)
