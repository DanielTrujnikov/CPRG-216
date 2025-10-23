# string = a sequence of indexed characters used for text
# List – a collection of values which is indexed, ordered, and changeable
# Tuple – a collection of values which is indexed, ordered, and unchangeable
# Dictionary – a collection of key-value pairs which is indexed, unordered, and changeable
# Set – a collection of unique values which is unordered and unindexed

course = "CPRG 216 - OOP 1"
greeting = 'Welcome in'
print(greeting,course)
print('first char = ', greeting[0]) # first char = W
print('# of chars = ', len(greeting)) # # of chars =  10
print('last char = ', greeting[9]) # last char =  n
print('last char = ', greeting[len(greeting)-1]) # last char =  n

data = [3,4,5]
data[2]

print(data)
print(data[2])


# LIST EXAMPLE
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")     # add
fruits[0] = "mango"         # change
print(fruits)  # ['mango', 'banana', 'cherry', 'orange']

# TUPLE EXAMPLE
fruits = ("apple", "banana", "cherry")
# fruits.append("orange")   # ❌ Error: tuples do not have append method
# fruits[0] = "mango"  # ❌ Error: tuples are immutable
print(fruits)  # ('apple', 'banana', 'cherry')

data = [1, 2, 3, 4, 5]
week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

for item in data:
    cubed = item**3
    print(item, cubed)

for day in week:
    print(day)

l = len(week)
print(l)

print (list(range(7)))

for i in range(len(week)):
    print(week[i])

# len
nums = [1, 8, 2, 3, 3, 4, 8, 5]
n = len(nums) # counts the number of numbers in the brackets in nums =
print(len(nums))

# count function
print(nums.count(3)) # prints the amount of 3's in the brackets

# list function # convertes a data structure into a list
numbers = list(range(11))
T = (1, 2, 3, 4, 5,)
L = list(T)

print(L) # list
print(T)

for n in numbers:
    print(n, end =" ")

for t in T:
    print(t, end =" ")

for l in L:
    print(l, end =" ")

# pop, remove and del
print(nums)
nums.remove(4) # removes the first instance of 4
print(nums)
del nums [4] # removes the number at index 4
print(nums)
nums.pop(0) # removes the number at index 0
print(nums)


'''
g = 'go FLAMES go'
print ('capitalize method') # Capitalize first letter of the string
print (g.capitalize())
print ('title method') # Capitalize first letter of each word in the string
print (g.title())
print ('lower method') # Convert all characters to lowercase
print (g.lower())
print ('upper method') # Convert all characters to uppercase
print (g.upper())
print ('swapcase method') # Swap the case of each character in the string
print (g.swapcase())
'''