def differenceSum(n):

    a=[]

    b=[]

    k=str(n)

    for i in range(len(k)):

        if int(i)%2==0:

        	a.append(int(k[i]))

        else:

        	b.append(int(k[i]))

    s=sum(b)

    r=sum(a)

    j=s-r

    return j
