def add(x,y):
    return x+y

print(add(3,4))

add = lambda x,y : x+y
nums = [1,2,3,4]
add_one = lambda x : x+1
new_nums = map(add_one,nums) # map is a special data structure func
print(nums)
print(list(new_nums))
add(2,4)

# lambda func should be used with small functions
# it is very important with functions that work on data structures

# you have a list of numbers that are not naturally sorted
# students 