def is_power_of_four(n):

    if n <= 0:

        return False

    while n > 1:

        if n % 4 != 0:

            return False

        n //= 4

    return True



# Test the function

n = int(input())

print(is_power_of_four(n))
