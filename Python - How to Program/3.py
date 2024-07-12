'''Self-review Exercises

3.1

a) multiple-selection
b) keywords
c) indefinite repetition
d) (repeated) multiplication
e) range
f) algorithm
g) pass
h) suite/body (?)
i) sequence, selection, repetition
j) flowchart


3.2

a) False
b) True
c) False
d) False
e) True
f) True
g) False
h) False
i) False
j) False

'''


# 3.3: Mileage Calculator

# Initialize variables for the final mileage display
total_gallons = 0
total_miles = 0

# initialize infinite while loop
while True:

    # Create variables to accept and store driver input
    gallons = float(input("Enter the gallons used (-1 to end): "))

    # sentinel value - is it possible to do this without break?
    if gallons == -1:
        break

    miles = float(input("Enter the miles driven: "))

    print()

    # show mileage for the trip
    if miles == 0:
        print("There was no travel on this trip. Cannot calculate mileage.\n")

    elif gallons != 0:
        print(f"The miles / gallon for this tank was {miles/gallons:.6f}.\n")

    else:
        print("It appears no gas was used on this trip. Congrats on your sustainable travel!\n")

    # add trip info to final mileage variables
    total_gallons += gallons
    total_miles += miles

print()

# show the overall average mileage
if total_miles == 0:
    print("There was no travel. Cannot calculate mileage.")

elif total_gallons != 0:
    print(f"The overall average miles/gallon for this vehicle was {total_miles/total_gallons:.6f}")

else:
    print("No gas was used on any of your trips. It appears you've truly unlocked infinitely sustainable travel. "
          "We will be seeing you soon.")

print("\n")

# worth noting that this code does calculations with floats, which is a no - no


# 3.4 Palindrome Checker

# open a loop so the user can try again if their input is invalid
while True:

    # Create a variable to accept potential palindromes
    num = input("Enter a five-digit integer: ")

    # Ensure the input follows the given parameters - delete this wrap to generalize
    if num.isdigit() and len(num) == 5:

        # Determine whether the input is a palindrome
        if num == num[::-1]:
            print("This number is a palindrome!")
        else:
            print("This number is not a palindrome :(")

        break

    # Guide the user towards entering a valid potential palindrome
    else:
        while num.isdigit() == 0 or len(num) != 5:
            print("This checker only evaluates 5 digit integers\n")
            break

print("\n")

# 3.5 Binary to Decimal Converter

# initialize variable for final decimal output
decimal = 0

# let the user input a binary number
binary = input("Enter a binary number: ")
index = len(binary) - 1

# convert each binary digit to a decimal value based on its position and add it to the decimal total
for digit in binary:
    digit = int(digit) * (2 ** index)
    decimal += digit
    index -= 1

print(f"This number in decimal form is {decimal}")

print("\n")

# 3.6 Factorials

# a) calculate factorials
def factorial(num):

    # result variable
    facto = 1

    # if input is non-negative
    if num > -1:

        # calculate factorial
        for i in range(1, num + 1):
            facto *= i
        return facto

    else:
        return "undefined"


number = int(input("Enter a non-negative integer: "))
print(f"The factorial of {number} is {factorial(number)}")

print("\n")

'''
# b) estimate 'e'
e = 1

for n in range(1, 10):
    e += 1/factorial(n)

print(e)
print()
'''

# c) compute e^x (highly inaccurate, again because of floats and rounding)

e_x = 1
x_count = 1
x = int(input("to what power would you like to raise mathematical constant 'e'? "))
print()

for a in range(1, 10):
    e_x += (x ** x_count) / factorial(a)
    x_count += 1

print(f"e^{x} = {e_x}")

# 3.7 Asterisk Patterns with For loops
#  3.8 Pythagorean Triples (when you feel like)

