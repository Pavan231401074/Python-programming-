a=int(input())

for i in range(2,a):

    if(a%2==0):

        flag=0

    elif(a%i!=0):

        flag=1

    else:

        flag=0

if(flag==1):

    print("2")

elif(flag==0):

    print("1")
