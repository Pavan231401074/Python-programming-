

a=input()

b=input()

C=''

d=int(input())

for i in range(len(a)):

    if(len(C)-d==0):

        break

    else:

        if(a[i]in b):

            if(a[i] not in C):

                C+=a[i]

print (C)
