user_input = input("Type in a month:")

months_31 = ["January", "March", "May", "July", "August", "October", "December"]
months_30 = ["April", "June", "September", "November"]
feburary = "February"

if user_input in months_31:
    print(user_input, "has 31 days")
elif user_input in months_30:
    print(user_input, "has 30 days")
elif user_input == feburary:
    print(user_input, "has 28 or 29 days")
else: print(user_input, "is not a month")