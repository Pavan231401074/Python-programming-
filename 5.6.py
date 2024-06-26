import sys

import math

 

def find_factors(n):

	factors = []

	for i in range(1, int(math.sqrt(n)) + 1):

    	if n % i == 0:

        	factors.append(i)

        	if i != n // i:

            	factors.append(n // i)

	return sorted(factors)

 

def get_pth_factor(n, p):

	factors = find_factors(n)

	if p <= len(factors):

    	return factors[p - 1]

	else:

    	return 0

 

# Reading input directly from the standard input (typically for competitive programming)

input = sys.stdin.read

data = input().split()

n = int(data[0])

p = int(data[1])

 

# Calculate and print the p-th factor

print(get_pth_factor(n, p))
