# compute the circumference of a circle 
# assume radius is 5
# modify the code so that it computes the area of the circle as well
# and that pi is 3.14

r = 5
PI = 3.14
# PI
#  = 22/7 logical error, cause if you want pi to be constant, you should not change its value

user_input = input("Please enter the radius of the circle: ")
print("Type of user input ", type(user_input))
int(user_input) # cast user input to an integer
r = int(user_input) # reassign r to the user input value

circumference = 2 * PI * r
print("The circumference of the circle is", circumference)

circle_area = PI * r**2
print("The circle area is", circle_area)