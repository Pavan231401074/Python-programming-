

n=int(input())

l=[]

k=[]

while n>0:

    a=n%10

    n=n//10

    l.append(a)

for i in range(len(l)):

    if l.count(l[i])==1:

        k.append(l[i])

print(len(k))
