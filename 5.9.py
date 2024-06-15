def find_element_locations(lst, target):

    locations = []

    count = 0

    for i in range(len(lst)):

        if lst[i] == target:

        	locations.append(i + 1)

        	count += 1

   

    return locations, count

 

def main():

    n = int(input())

    lst = [int(input()) for _ in range(n)]

    target = int(input())

 

    locations, count = find_element_locations(lst, target)

 

    if count == 0:

        print(f"{target} is not present in the array.")

    else:

        for loc in locations:

        	print(f"{target} is present at location {loc}.")

        print(f"{target} is present {count} times in the array.")

 

if __name__ == "__main__":

    main()
