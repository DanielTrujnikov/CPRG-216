# sets 

data = {1, 2, 3, 4, 5}
data.add(6) # adding an element
data.remove(3) # removing an element
print(data)
dataset = set(data) # converting list to set
print(dataset) # printing the set

text = "hello world"
unique = set(text) # converting string to set
print(unique) # printing the set
# sets are unordered collections of unique elements
# they do not allow duplicate values
# they support mathematical operations like union, intersection, difference
for char in unique:
    print(char, end="\t")
for char in unique:
    print(char, end="\t")

print(min(data)) # minimum value in the set
print(max(data)) # maximum value in the set
print(len(data)) # length of the set
del data # deleting the set

num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7, 8}
'''
num3 = num1.intersection(num2) # intersection of two sets
num4 = num1.union(num2) # union of two sets
num5 = num1.difference(num2) # difference of two sets
print(num3)
print(num4)
print(num5)
'''
num3 = num1 & num2 # intersection of two sets
num4 = num1 | num2 # union of two sets
num5 = num1 - num2 # difference of two sets
print(num3)
print(num4)
print(num5)

# bitwise operators
n = 4 & 3
print(n) # which ones match in binary
# 4 = 00000100
# 3 = 00000011
# & = 00000000 = 0
n = 4 | 3
print(n) # which ones are present in binary
# 4 = 00000100
# 3 = 00000011
# | = 00000111 = 7
n = 4 ^ 3 # which ones are different in binary
print(n)
# 4 = 00000100
# 3 = 00000011
# ^ = 00000111 = 7

text = "      hello lil bro  "
print(text)
print(text.strip()) # removes leading and trailing spaces