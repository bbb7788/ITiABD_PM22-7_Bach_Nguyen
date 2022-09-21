import random
a = []
b = []
c = []
for i in range(random.randint(1,15)):
    a.append(random.randint(1,299))
print(a)
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
b.sort()
c.sort()
print(b)
print(c)