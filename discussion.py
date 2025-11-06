# 1- a function that takes three arguments and return the maximum of them.

print("Please enter three numbers\n")
x = float(input("Enter first number\n"))
y = float(input("Enter second number\n"))
z = float(input("Enter third number\n"))

def my_max(x, y, z):
    if x >= y and x >= z:
        print(x)
    elif y >= x and y >= z:
        print(y)
    else:
        print(z)
print("The maximum number is:")
my_max(x, y, z)

# 2-a function that takes a name and year of birth, and print a welcome message and the computed age (it does not return anything)

input_name = input("Please enter your name\n")
input_year = int(input("Please enter your year of birth\n"))
def welcome_message(name, year):
    current_year = 2025
    age = current_year - year
    print(f"Welcome {name}! You are {age} years old.")
welcome_message(input_name, input_year)

# 3- a function that computes the square root of an argument

number = float(input("Please enter a number to compute its square root\n"))

def compute_sqrt(num):
    sqrt = num ** 0.5
    return sqrt # return the computed square root
result = compute_sqrt(number) # call the function and store the returned value
print(f"The square root of {number} is {result}")