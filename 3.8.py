

a=int(input())

b=int(input())

c=int(input())

if(a*a+b*b==c*c):

    print("yes")

elif(a*a+c*c==b*b):

    print("yes")

elif(c*c+b*b==a*a):

    print("yes")

else:

    print("no")
