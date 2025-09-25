# 3rd class
'''
In this class we will work on variables, operators, and other stuff
'''

# review
# assignment

x = 5 # integer
print(x, type(x))
y = 6.7 # float
print(y, type(y))
z = "Hello" # string
print(z, type(z))
a = True # boolean
print(a, type(a))

# some functions call : print, input, int, float, str, bool
num_as_text = "43"

num_as_num = int(num_as_text)

print(num_as_text)
print(num_as_num)
print(str(num_as_num))

num = 3
num_f = float(3)

num2 = 3.4
num2_i = int(num2)

num2_as_text = str(num2)

# using input function... not input function always returns a string

'''
year_of_birth = input("Please enter your year of birth: ")
year_of_birth = int(year_of_birth)
print("Your age is", 2025 - year_of_birth)
'''
# print function

print("Hello", "World", sep=' ', end=', ')
print("Hello", "World", sep=' ')
print("Hello\tworld") # tab space
print("Hello\nworld") # new line
print('What is the student\'s name?') # escape character
print("Use this symbol \\ to make an escape character")

# precedence rules

expression = 3+4*0-300+12/3
print(expression)

expression = 4/2*3
print(expression)

# more about assignments

x = 3
x = x + 5

print(x)

# can we have a shorthand for this expression?

x += 5 # x = x + 5

# other expressions

x -= 2 # x = x - 2
print(x)
x *= 3 # x = x * 3
print(x)
x /= 4 # x = x / 4
print(x)
x **= 2 # x = x ** 2
print(x)