weekend = ["Saturday", "Sunday"]
data = []
nums = [1, 2, 3, 4]
measurements = [3.4, 2.4]
status = [True, False, False, True]
objects = ["Hello", 2, False, 4.5] # mixed data types

condition = "Hello" in objects # checks if "Hello" is in objects list
print(condition)

for num in nums:
    print(num ** 2, end='\t')

print()
print(nums[3])  # first element
nums[3] = 18 # modify element at index 3

for num in nums:
    print(num, end='\t')

for i in range(0,len(nums)): # range will generate numbers from 0 to len(nums)-1
    print(nums[i], end='\t')

print()

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = num1 + num2 # concatenation of two lists
print(num1, num2, num3)

num1.append(4) # adds 4 at the end of num1
print(num1)
num1.extend([5, 6, 7]) # extends num1 by adding multiple elements at the end
print(num1)

options = ["Yes", "Y", "y"]
user_input = input("Do you want to continue?y/n\n")
if user_input in options:
    print("Continue")

# TUPLE EXAMPLE
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(days[0])
# days[0] = "Sun"  # ❌ Error: tuples are immutable

days_ = list(days)  # convert tuple to list
days_.append("Sat")  # now we can append to the list
print(days_)
some_days = tuple(days_)  # convert back to tuple
print(some_days)

print(num1)
del num1[3]  # deletes element at index 3
print(num1)
num1.pop(4)  # removes element at index 4
print(num1)
del num1  # deletes the entire list
# print(num1)  # ❌ Error: num1 is deleted
print("num3:", num3)
num3.clear()  # removes all elements from num3
print("num3 after clear:", num3)
x = 30
del x  # deletes variable x
# print(x)  # ❌ Error: x is deleted

vowel = ['a', 'e', 'i', 'o', 'u']
text = "Hello, how are you?"

for character in text:
    if character in vowel:
        print(character, "is a vowel")
    else:
        print(character, "is not a vowel")

random = [3, 6, 2, 8, 4, 10, 12, 5]
# random.sort()  # sorts the list in ascending order
print(random)
ordered = sorted(random) # returns a new sorted list
print(ordered)

# copying data
n1 = [1, 2, 3, 4, 5]
n2 = n1  # both n1 and n2 refer to the same list
n1[2] = 4
n2[0] = 3
print(n1, n2)  # both reflect the changes

m = n1.copy()  # creates a shallow copy of n1
m[0] = 7
n1[1] = 9
print(n1, n2, m)  # m is independent of n1

text = "Hello World!"
words = text.split(" ")  # splits the string into a list
print(words)
words = ['John', 'Doe', 'is', 'a', 'developer']
names = " ".join(words)  # joins the list into a string
print(names)

print(max(random))  # maximum value in the list
print(min(random))  # minimum value in the list
print(sum(random))  # sum of all elements in the list
print(len(random))  # number of elements in the list

print(ordered)
ordered.insert(5,6)  # inserts 6 at index 5
ordered.insert(6,7)  # inserts 7 at index 6
print(ordered)

attendance = [True, False, True, True, False, True]
print(attendance.count(True))  # counts how many times True appears in the list
print(attendance.count(False))  # counts how many times False appears in the list
print(ordered.index(10))  # returns the index of the first occurrence of 10

print(random[:5]) # from start to index 4
print(random[2:7]) # from index 2 to index 6
print(random[5:]) # from index 5 to the end

gpa = []
gpa.append(3.5)
gpa.append(3.8)
gpa.append(4.0)
print(gpa)
average = sum(gpa) / len(gpa)
print("Average GPA:", average)


# Tuple example

data = () # cannot be modified
data = (1, 2, 3) # cannot be modified
print(data)

weekend = ("Saturday", "Sunday")
day = ("Monday",) # single element tuple
print(type(day))

x = 3 
x = (3+1)/3
print(type(x))
print(day[0])

for day in weekend:
    print(day)
# weekend[0] = "Fri" # ❌ Error: tuples are immutable

age = 13
name = "John"
city = "Calgary"

info = (age, name, city) # packing
print(info)

info_list = [age, name, city] # list packing
print(info_list)

things = ("car", 3.5, True, 10)
'''decice = things[0]
count = things[1]
measurement = things[2]
status = things[3]
print(decice, count, measurement, status)
'''
# unpacking
device, count, measurement, status = things
print(device, count, measurement, status)

things_ = list(things) # convert tuple to list
things_again = tuple(things_) # convert list back to tuple
print(things_, things_again)

# concat tuples
val1 = (1, 2, 3)
val2 = (4, 5, 6)
val3 = val1 + val2
print(val3)

print(val3[:3]) # from start to index 2
print(val3[3:]) # from index 3 to end

# dictionary example
temperatures = {1: 32, 2: 45, 3: 50}
print(temperatures[2])
gpas = {"John": 3.5, "Alice": 3.8, "Bob": 4.0}
print(gpas["Alice"])