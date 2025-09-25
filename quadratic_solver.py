A = int(input("Please enter a value for a: "))
B = int(input("Please enter a value for b: "))
C = int(input("Please enter a value for c: "))
x1 = 0
x2 = 0
if A == 0:
    x1 = x2 = -C / B
elif B**2 - 4*A*C >= 0:
    from math import sqrt
    x1 = (-B + sqrt(B**2 - 4*A*C)) / (2*A)
    x2 = (-B - sqrt(B**2 - 4*A*C)) / (2*A)
else:
    print ("No possible solution")
print ("The solutions are", x1, "and", x2)