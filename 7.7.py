def checkUgly(n):

	for i in range(n):

    	for j in range(n):

        	for k in range(n):

            	if(n==(2**i)+(3**j)+(5**k)):

                	return("ugly")

	return("not ugly")
