a=int(input())

l=[]

l.extend(input().split())

for i in range(a-1):

    for j in range(a-1):

        if(int(l[j])>int(l[j+1])):

            t=int(l[j])

            l[j]=int(l[j+1])

            l[j+1]=t

for i in range(a):

    print(int(l[i]),end=" ")
