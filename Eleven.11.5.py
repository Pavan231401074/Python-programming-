    a=float(input())

    if(a<0):

        print("Error: Cannot calculate the square root of a negative number.")

    else:

        print("The square root of",a,"is {:.2f}".format(a**0.5))

except:

    print("Error: could not convert string to float")
