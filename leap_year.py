print("Have you ever wondered if a year is a leap year?")
print("Today we will find out if a year is a leap year or not!")
year = int(input("Enter a year: "))

if year % 4 == 0:
    print(year, "is a gap year")
if year % 100 == 0:
    print(year, "is a century")
else:
    print(year, "is not a special year")