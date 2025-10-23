# Dictionary

months = {1:"January", 2:"February", 3:"March"}
print("The second month is", months[2])

student_data = {"Diddy":4.0, "Epstein":3.7} # name: gpa
print("Diddy's GPA is", student_data["Diddy"])

nums = [1,2,3,4]
nums2 = (1,2,3,4)

print(nums[1])  # lists are mutable
print(nums2[-1]) # tuples are immutable

print(student_data.keys())
print(student_data.values())

avg_temp = {1:28.3, 2:23.4, 3:25.2, 4:30.0, 5:3.3, 6:26.4, 7:23.5}
print(avg_temp) # entire dictionary
print(avg_temp.keys()) # all keys
print(avg_temp.values()) # all values
print(avg_temp[3]) # value for key 3

for day in avg_temp: # by default iterates over keys
    print(day, avg_temp[day])

for day, temp in avg_temp.items(): # iterates over key-value pairs
    print(day, temp)


frequency = dict()

text = "What is good homie"
print(text[3])


for ch in text:
    if frequency.get(ch) == None:
        frequency[ch] = "*"
    else:
        frequency[ch] += "*"

for ch in frequency:
    print(ch,": ", frequency[ch])