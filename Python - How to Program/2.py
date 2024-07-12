# Ex. 2: Print multiple lines of code with 1 statement

print("welcome\nto\nPython!\n")


# Ex. 3: Adding integers

integer1 = int(input("Enter first integer: "))  # accept user input and convert to int
integer2 = int(input("Enter second integer: "))

Sum = integer1 + integer2  # compute and assign sum

print("\nSum is", Sum, "\n")  # print sum


# Ex. 4: String Formatting (quote marks)

print(
    "This is a string with \"double quotes\"\n"
    'This is another string with "double quotes"\n'
    'This is a string with \'single quotes\'\n'
    "This is another string with 'single quotes'\n"
    """This string has "double quotes" and 'single quotes'.
     You can even do multiple lines.\n"""
    '''This string also has "double" and 'single' quotes'\n'''
)

'''
Self-review exercises

2.1
a) print
b) string
c) identifiers
d) %
e) comments
f) if, condition, colon, body
g) int
h) \
i) parentheses
j) type

2.2
a) false. the function is input()
b) false. rules of precedence and associativity
c) true (start with numbers)
d) true
f) false. variable/object type does that
g) false. python uses dynamic typing
h) true
i) false. case matters in python
j) false. escape character. escape sequence when paired
k) true


# 2.3: Order of Ops

# a) multiplication division addition subtraction: 15

print(7 + 3 * 6 / 2 - 1)

# b) mod mult div add sub: 3

print(2 % 2 + 2 * 2 - 2 / 2)

# c) lastmult div add mult mult:

print(27 * 12)
print((3 * 9 * (3 + (9 * 3 / (3)))))

print("\n")
'''

# 2.4: SPDQ

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print()

print(f"sum: {num1 + num2}\nprod: {num1 * num2}\ndiff: {num1 - num2}\nquot: {num1 / num2}")

print( )


# 2.5: Circle

rad = int(input("Enter radius of circle: "))
pi = 3.14159

print(f"\ndiameter: {rad * 2}\ncircumference: {rad * 2 * pi}\narea: {rad * rad * pi}\n")


# 2.6: Print shapes

shape = input("Shape? ")
a = "*"
b = " "
n = "\n"

print()

if shape == "box":
    print(("\n") + ("*" * 9) + ("\n*" + " " * 7 + "*") * 7 + ("\n") + ("*" * 9))

elif shape == "oval":
    print((" " * 3 + "*" * 3 + " " * 3) + ("\n *" + " " * 5 + "*") + ("\n*" + " " * 7 + "*") * 5\
          + ("\n *" + " " * 5 + "*") + "\n" + (" " * 3 + "*" * 3 + " " * 3))

elif shape == "arrow":
    print((b * 2 + a + b * 2) + n + (b + a * 3 + b) + n + (a * 5) + (n + b * 2 + a + b * 2) * 6)

elif shape == "diamond":
    print((b * 4 + a + b * 4) + n + (b * 3 + a + b + a + b * 3) + n + (b * 2 + a + b * 3 + a + b * 2) +
          n + (b * 1 + a + b * 5 + a + b * 1) + n + (a + b * 7 + a) + n + (b * 1 + a + b * 5 + a + b * 1) +
          n + (b * 2 + a + b * 3 + a + b * 2) + n + (b * 3 + a + b + a + b * 3) + n + (b * 4 + a + b * 4))

else:
    print("Sorry, shape not supported")

print(" ")


# 2.7 Multiple checker

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another: "))

if num1 % num2 == 0:
    print(f"{num1} is a multiple of {num2}")

elif num1 % num2 != 0:
    print(f"{num1} is NOT a multiple of {num2}")

else:
    print("ERROR")





