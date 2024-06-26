

def bubble_sort(arr):

    n = len(arr)

    swaps = 0

    

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1]:

                # Swap elements

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swaps += 1

    

    return swaps



# Input the size of the list

n = int(input())



# Input the list of integers

arr = list(map(int, input().split()))



# Perform bubble sort and count the number of swaps

num_swaps = bubble_sort(arr)



# Print the number of swaps

print("List is sorted in", num_swaps, "swaps.")



# Print the first element

print("First Element:", arr[0])



# Print the last element

print("Last Element:", arr[-1])
