a=int(input())

d={}

for i in range(a):

    b=input()

    b=b.partition(" ")

    d[b[0]]=b[-1].split(" ")

n=list(d.values())

k=list(d.keys())

for i in range(len(n)):

    s=0

    for j in range(len(n[i])):

        s+=int(n[i][j])

    d.update({k[i]:s})

l=list(d.items())

if(l[0][1]<l[1][1]):

    for k,v in d.items():

        print(k,v)

else:

    j=1

    for k,v in d.items():

        if(j==1):

            k1,v1=k,v

            j+=1

        else:

            print(k,v)

    print(k1,v1)
