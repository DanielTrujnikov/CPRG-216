'''
yesterday = 0.7588
today = 0.7479
change = today - yesterday

print ("{:>9s} {:>9s}".format("Date", "Rate")) # right align with 9 spaces
print ("{:>9s} {:>9s}".format("====", "====")) # right align with 9 spaces
print ("{:>9s} {:>9.4f}".format("Yesterday", yesterday)) # right align with 9 spaces and 4 decimal places
print ("{:>9s} {:>9.4f}".format("Today", today)) # right align with 9 spaces and 4 decimal places
print ("{:>9s} {:>9.4f}".format("Change", change)) # right align with 9 spaces and 4 decimal places
'''

names = ["Alice", "Bob", "Catherine", "Daniel"]
grades = [85, 92, 78, 99]

print (f"{'GPA table':^24}") # center align with 24 spaces
print (f"{'Name':>10s}{'Grades':>8s}") # right align with 10 and 8 spaces
print (f"{'====':>10s}{'====':>6s}") # right align with 10 and 6 spaces
for i in range(4):
    print (f"{names[i]:>10s}{grades[i]:>6.1f}")

s = 300000000
print (f"{s:.2e}") # scientific notation with 2 decimal places and commas
print (f"{s:,%}") # percentage notation
print (f"{s:,.2f}") # fixed point notation with 2 decimal places

name = "Owen"
age = 67
gpa = 3.672
text = "The name is {}, The age is {}, The GPA is {:.2f}".format(name, age, gpa) # the {} will take it in order from the ()
print (text)

text = f"The name is {name}, The age is {age}, The GPA is {gpa:.2f}"
print (text)