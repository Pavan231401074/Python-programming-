a=input()

d=[]

b=input()

c=input()

b=tuple(b.split(" "))

c=tuple(c.split(" "))

for i in b:

    if i not in c:

        d.append(i)

for i in c:

    if i not in b:

        d.append(i)

for i in range(len(d)):

    print(int(d[i]),end=' ')

print()

print(len(d))
