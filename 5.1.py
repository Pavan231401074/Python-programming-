a=int(input())

l=[]

for i in range(a):

    c=int(input())

    l.append(c)

for i in range(1,a):

    d=sum(l[0:i])

    r=sum(l[i+1:])

    if(d==r):

        print(i)
