# Range : it is a sequence generator
# Range have 3 values = range(start, stop, step) , default = start is 0. and step is +1
# range(1,6) => 1,2,3,4,5 and it stops when 6 came and don't print 6 in it
# range(1,6,2) => it means +2 =  1,3,5


# for i in range(1,6):
#     print(i)

# for i in range(1,6,2):
#     print(i)


# print sum of n natural number

n = int(input("Enter number: "))
sum = 0
for i in range(1, n + 1):
    sum += i

print("sum =", sum)