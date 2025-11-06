def square(x):
    return x**2

print(square(5))

x = print("Hello, World!")
print(x)  # This will print 'None' because print() returns None

def write_to_file(file): # function with input and no output
    fid = open(file, 'a') # open file in append mode
    fid.write("Hello\n") # write "Hello" to the file
    return None # The function does not return anything meaningful

write_to_file("new.txt")
print(write_to_file("another_file.txt"))

# no input but with output

import random
print("Please enter your name:")
name = input()
print("Hello", name)

def generate_random():
    return random.randint(1, 10) # function that returns a random integer between 1 and 10

for i in range(1, 101): # loop to print 100 random numbers
    print(generate_random()) # print the random number generated