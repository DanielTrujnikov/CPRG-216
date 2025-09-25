print ("Welcome to the grade calculator")

grade = int(input("Enter your grade from (0-100): "))

if grade >= 90:
    print("Your grade is a A")
    print("Great job!")
elif grade >= 80:
    print("Your grade is a B")
    print("Good job!")
elif grade >= 70:
    print("Your grade is a C")
    print("You passed!")
elif grade >=60:
    print("Your grade is a D")
    print("You need to work harder!")
else:
    print("Your grade is a F")
    print("You're dumb!")


