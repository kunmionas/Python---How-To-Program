'''
5.1
a) dictionaries, key-value
b) -1
c) tup1 = item,
d) len
e) slicing
f) .items()
g) by value
h) sequence[i, j + 1]
i) m by n sequence
j) .count()

5.2
a) f
b) f
c) t
d) f
e) f
f) f
g) t
h) t
i) f
j) t
'''


# 5.5 Sieve of Eratosthenes

def sieve_of_eratosthenes(gap):

    potentials = {}
    primes = []

    for i in range(2, gap):
        potentials.update({i: True})

    for key, value in potentials.items():  # outer loop
        if value:
            for key2, value2 in potentials.items():  # inner loop
                if value2:
                    if key2 % key == 0:
                        if key == key2:
                            continue
                        potentials[key2] = False

    for key3, value3 in potentials.items():
        if value3:
            primes.append(key3)
    return primes


user_gap = int(input("Enter a number: "))
print(f"There are {len(sieve_of_eratosthenes(user_gap))} prime numbers between 0 and {user_gap}\n")


# 5.6 Bubble Sort

def bubbleSort(list1):

    n = len(list1)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                swapped = True
        if not swapped:
            break


# Driver code to test above
arr = input("Enter a list of random, comma separated numbers: ").split(",")

arr = list(map(int, arr))
bubbleSort(arr)

print(f"BubbleSorted list: {arr}\n")



# 5.7 Binary Search

def binarysearch(search_key, list2):

    if len(list2) == 1 and list2[0] != search_key:
        return "\nThis number is not in the list"

    mid_index = len(list2)//2
    mid_value = list2[mid_index]

    if mid_value == search_key:
        return mid_index + 1

    elif mid_value > search_key:
        return binarysearch(search_key, list2[:mid_index])

    else:
        result = binarysearch(search_key, list2[mid_index + 1:])
        if result == "\nItem is not in list":
            return result
        return mid_index + 1 + result


# Example call:
import random
example_list = sorted([random.randrange(1, 1000) for _i in range(500)])
print("I have a list containing 500 numbers between 0 and 1000")

key = int(input("What number would you like to search this list for? "))

result = binarysearch(key, example_list)

if type(result) == int:
    print(f"\n{key} was found in the list at position {result}")

else:
    print(result)










