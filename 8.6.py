a=input()

b=input()

c=set()

for i in a:

    for j in b:

        if j in i:

            c.add(i)

print(len(c))
