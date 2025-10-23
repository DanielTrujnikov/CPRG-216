print ("Welcome to GPA average grade calculator")


continue_option = "y"
while continue_option == "y":
    print("Please enter three numbers:")
    a = float(input(""))
    b = float(input(""))
    c = float(input(""))

    sum = a + b + c
    average = sum / 3

    print("The average is", average)
    continue_option = (input("Would you like to continue?y/n\t"))

print("Exiting...")
    