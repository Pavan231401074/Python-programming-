

a,c=[],[]

for i in range(0,5):

    b=input()

    a.append(b)

for i in range(len(a)):

    if(a[i] not in c):

        c.append(a[i])

        print(a[i])
