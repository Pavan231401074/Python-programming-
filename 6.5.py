

a=[]

a=input()

b=a. split()

for i in b:

    k=i.lower()

    if k!=k[::-1]:

         print(k,end=' ')
