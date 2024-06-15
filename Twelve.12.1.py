def count_pairs_with_difference_k(activities, k):

    count = 0

    n = len(activities)

    for i in range(n):

        for j in range(i + 1, n):

            if abs(activities[i] - activities[j]) == k:

                count += 1

    return count



# Reading input

n = int(input())

activities = list(map(int, input().split()))

k = int(input())



# Calling function and printing the result

print(count_pairs_)
