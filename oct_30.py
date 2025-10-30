'''
def my_max():
    print("Please enter two numbers\n")
    x = float(input("Enter first number\n"))
    y = float(input("Enter second number\n"))

    if x < y:
        print(y)
    else:
        print(x)

print ("Random message")

def compute_area(r):
    PI = 3.14
    area = PI*r**2
    print(area)

compute_area(1)


my_max()
my_max()
my_max()
# print random message
# print random message
my_max()
# print random message
'''

def my_max(x, y):
    max = y
    if x > y:
        max = x
    return max

print (my_max(6, 7))
m = my_max(10, 5)
print (m)

l = 4
n = 33
m = my_max(l, n)
print (m)
