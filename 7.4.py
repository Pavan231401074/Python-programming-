def christmasDiscount(n):

    res=0

    while n!=0:

        rem=n%10

        flag=0

        for i in range(1,rem+1):

            if rem%i==0:

                flag+=1

        if flag==2:

            res=res+rem

        n=n//10

        

    return res
