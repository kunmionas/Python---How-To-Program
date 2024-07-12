'''
4.1
a) Divide and conquer
b) functions, classes, modules and packages
c) modules/libraries
d) math
e) def
f) parentheses
g) random
h) _name_
i) local, global and built-in
j) base case

4.2
a) f
b) f
c) t
d) f
e) t
f) f
g) t
h) f
i) t
j) t
'''

# 4.3 Celsius to Fahrenheit
def fahrenheitenator(C):

    C = int(C)
    F = 9 / 5 * (C) + 32
    return f'C:{C:^6d} F:{F:.2f}'


C = input("Enter a temperature in celsius: ")
print(fahrenheitenator(C))

print()


# 4.4 Prime Numbers
def prime_check(num):

    if num < 2:
        return f"{num} is not a prime number :("

    for factor in range(2, int(num**0.5) + 1):

        if num % factor == 0:
            return f"{num} is not a prime number :("

    return f"{num} is a prime number!"


num = int(input("Enter a number: "))
print(prime_check(num))

print()


# 4.5 Perfect Numbers
def perfect(number):

    if number <= 0:
        return False

    sum_of_factors = 0

    for factor in range(1, int(number/2 + 1)):

        if number % factor == 0:

            sum_of_factors += factor

    if sum_of_factors == number:
        return True


gap = int(input("What range of numbers would you like to search for perfect numbers? "))

perfects = []

for i in range(gap):
    if perfect(i):
        perfects.append(i)

if len(perfects) > 1:
    perfects.insert(-1, "and")
perfects = ", ".join(map(str, perfects))
if len(perfects) > 1:
    perfects = list(perfects)
    perfects.reverse()
    perfects.remove(",")
    if len(perfects) > 5:
        perfects.remove(",")
    perfects.reverse()
    perfects = "".join(perfects)

if len(perfects) > 1:
    print(f"The perfect numbers between 0 and {gap} are {perfects}")
elif len(perfects) == 1:
    print(f"The only perfect number between 0 and {gap} is {perfects}")
else:
    print(f"There are no perfect numbers between 0 and {gap}")

print()


# 4.6 Teaching multiplication

def multiplication_teacher():
    from random import randrange

    num1 = randrange(1, 10)
    num2 = randrange(1, 10)

    while True:
        answer = input(f"What is {num1} times {num2}? ")

        print()

        if int(answer) == num1 * num2:
            print("Very good!\n")
            break

        else:
            print("No. Please try again\n")
            continue


rounds = int(input("How many rounds of multiplication would you like to practice? "))
for i in range(rounds):
    multiplication_teacher()

if rounds < 1:
    print()


# 4.7 Guess the number
def guess_the_number():

    from random import randrange

    guess_number = 2

    number = randrange(1, 1001)

    print("\nI have a number between 1 and 1000.\nCan you guess my number?\n")
    guess = int(input("Please type your first guess: "))

    while True:
        if guess == number:
            print("\nExcellent! You guessed the number!\n")
            while True:
                replay = input("Would you like to play again (y or n)? ")

                if replay == "y":
                    guess_the_number()

                elif replay == "n":
                    print("\nThanks for playing!\n")
                    return

                else:
                    print()
                    continue

        elif guess > number:
            print("\nToo high. Try again")
            guess = int(input(f"Guess {guess_number}: "))
            guess_number += 1
            continue

        else:
            print("\nToo low. Try again")
            guess = int(input(f"Guess {guess_number}: "))
            guess_number += 1
            continue


play = input("Would you like to play guess the number (y or n)? ")
if play == "y":
    guess_the_number()
else:
    print()


# 4.8 Towers of Hanoi
def towers_solver(n, initial, holding, final):

    if n == 1:  # base case
        print(f"{initial} --> {final}")
        return
    else:
        towers_solver(n-1, initial, final, holding)
        print(f"{initial} --> {final}")
        towers_solver(n-1, holding, initial, final)


n = int(input("I will now give you a solution to the Tower of Hanoi problem.\n"
              "How many disks would you like to solve for? "))
(towers_solver(n, 1, 2, 3))