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
print("What would you like to do?")
print("Type (a)dd (s)ubtract (m)ultiply (d)ivide or (q)uit")

user_choice =input(": ")

while user_choice == "q":
    print("Goodbye...")
    exit()

if user_choice not in ["a","s","m","d","q"]: 
    print("Invalid input")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if user_choice == "a":
    add(x, y)

elif user_choice == "s":
    subtract(x, y)

elif user_choice == "m":
    multiply(x, y)

elif user_choice == "d":
    divide(x, y)