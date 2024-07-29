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



# 5.5 Sieve of Eratosthenes

def sieve_of_eratosthenes(gap):

    potentials = {}
    primes = []

    for i in range(2, gap + 1):
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
print(f"There are {len(sieve_of_eratosthenes(user_gap))} prime numbers between 0 and {user_gap}")
'''

# 5.6 Bubble Sort
def bubbleSort(list1):

    item1 = 0
    item2 = 0

    for unit in list1:

        for comp in list1:
            if unit > comp:
                comp = unit

    return list1


lista = [3, 2, 1]
print(bubbleSort(lista))







