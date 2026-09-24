# Function that adds two numbers
def add(x,y):
    print(x+y)

# Function that subtracts two numbers
def subtract(x,y):
    print(x-y)

# Function that multiplies two numbers
def multiply(x,y):
    print(x*y)

# Function that divides two numbers
def divide(x,y):
    print(x/y)

print("Welcome")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

user_input =input("Would you like to (a)dd, (s)ubtract, (m)ultiply, or (d)ivide?: ")

if user_input == "a":
    print("add")
    add(x, y)

elif user_input == "s":
    print("subtract")
    subtract(x, y)

elif user_input == "m":
    print("multiply")
    multiply(x, y)

elif user_input == "d":
    print("divide")
    divide(x, y)

else: 
    print("Invalid input")


