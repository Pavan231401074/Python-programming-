

a=int(input())

flag=0

for i in range(10):

    for j in range(10):

        if(i*j==a):

            flag=1

            break

if(flag==1):

    print("Yes")

else:

    print("No")
