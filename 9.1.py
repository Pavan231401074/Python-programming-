a=input().split()

b=input().split()

c1,c2,l={},{},[]

for i in a:

    c1[i]=c1.get(i,0)+1

for j in b:

    c2[j]=c2.get(j,0)+1

for w,c in c1.items():

    if(c==1 and w not in b):

        l.append(w)

for w,c in c2.items():

    if(c==1 and w not in a):

        l.append(w)

print(*l)
