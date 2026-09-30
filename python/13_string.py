goal = "I want "
success = "success"
peace = "Peace"

print(goal + success + "and " + peace)
print(success[4:2])


# string are immutable (can not be change) in python
# slicing : string[starting index : ending index (but ending index is not included)]

# normal formatting
time = "my time will also come"

print("Quote = {}".format(time))

a = 5
b = 6
sum = a + b

# normal formating
# print("the sum of {} and {} is {}".format(a, b, sum))

# index formatting 
# print("the sum of {1} and {0} is {2}".format(a, b, sum))

# value base formatting
# print("the value of {a} and {b}".format(a=5, b=5))


# F-strings = literal string interpolation
print(f"sum of {a} and {b} is {a + b}")