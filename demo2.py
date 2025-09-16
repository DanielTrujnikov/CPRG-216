# variable
# variable has a name
# , has a value
# , has an address
# , has a size
# , and has a type

i = 3 # integer 
f = 4.5 # float
b = True # boolean
s = "Hello" # string 
ch = "a" # still a string

print(i,type(i))
print(f, type(f))
print(b, type(b))
print(s, type(s))
print(ch, type(ch))

# variable names
# can use letters, numbers, and underscores only (no commas or spaces)
# cannot start with a number
# it can start with an undercore but you should not do that since it has a different meaning in python
# use meaningful variable names

# example
circle_radius = 5
pi = 3.14
circle_radius = 6 # reassigning a new value to circle_radius
circle_area = pi * circle_radius * circle_radius

print("The area of the circle is", circle_area)

# operations 

a = 3 + 4
b = 4 - 3
c = 4 * 3
d = 3 / 4
e = 4 % 3 # modulus (remainder)
f = 3 ** 2 # exponentiation (3 to the power of 2)
g = 3 // 4 # floor division (quotient without the remainder)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))

# combining variables

h = a + b # read the assignment from right to left
# it mean evealuate a + b first, then assign the result to h

print("The value of h is", h)

# static type vs dynamic type

x = 5 # x is an integer
print(x, type(x))
x = 4.3 # changed x to a float
print(x, type(x))
x = "Hello" # changed x to a string
print(x, type(x))
x = True # changed x to a boolean
print(x, type(x))

# casting

x = 3 # integer
y = 4 # integer
z = x / y # division always results in a float

print(z)

# manual casting

int(z) # cast z to an integer
print(int(z)) # print the integer value of z

print(int("43")) # cast the string "43" to an integer
print(str(43)) # cast 43 to a string

x = 1
print(x, type(x))

y = float(x) # cast x to a float and assign it to y
print(y, type(y))

v = 4.3
print(v, type(v))
u = int(v) # cast v to an integer and assign it to u
print(u, type(u))