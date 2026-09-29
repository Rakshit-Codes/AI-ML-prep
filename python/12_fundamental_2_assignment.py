# Q1 Write a program that takes salary as input. Using conditional statements,
# calculate the final tax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%


# salary = int(input("Enter your Salary"))

# if salary < 30000 :
#     salary *= 0.95
#     print("Final salary after 5% tax:", salary)
# elif salary >= 30000 and salary <= 70000 :
#     salary *= 0.85
#     print("Final salary after 15% tax:", salary)
# elif salary > 70000 :
#     salary *= 0.75
#     print("Final salary after 25% tax:", salary)
# else :
#     print("wrong input")

#----------------------------------------------------------------
# Q2 Write a function that takes two integers a and b and prints all even
# numbers between them (inclusive)

# a = int(input("enter 1st number"))
# b = int(input("enter 2nd number"))

# def alleven(a, b):
#     for i in range(a ,b+1):
#         if i % 2 == 0:
#             print(i)

# alleven(a, b)
            
#----------------------------------------------------------------
# # Q3 Write a function that prints the digits of a number, n
# For eg:n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.
# [Hint - The right most digit of a number N is N%10.
# And to remove the right most digit from a number, we can do N = N / 10.]

# digits = int(input("enter number"))

# def fun(digits):
#     while digits > 0:
#         digit = digits % 10
#         print(digit)
#         digits = digits // 10

# fun(digits)

#----------------------------------------------------------------

# Q4 Write a function to return the count the number of digits in a number, n.

# number = input("enter number")

# def count(number):
#    print(len(number))


# count(number)
#----------------------------------------------------------------
# Q5 Write a function to return the sum of digits of a number, n.
# n = int(input("enter number"))

# def sum_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total = total + digit
#         n = n // 10

#     return total

# print(sum_digits(n))

#----------------------------------------------------------------
# Q6 Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5

# number = 1

# for i in range(number, 100+1):
#     if (i % 3 == 0 and i % 5 == 0):
#         print(i)

#----------------------------------------------------------------
# Q7 Design a program to continuously input a number n from user & print if it is
# positive or negative until the user enters “Quit”.


# while True :

#     user_input = input("enter number")

#     if user_input == "Quit":
#         break


#     user_input = int(user_input)

 

#     if (user_input > 0 or user_input < 0):
#         user_input = int(user_input)


#----------------------------------------------------------------
# Q8 Letʼs create a Simple calculator that performs arithmetic operations. Create a function calculator(a, b, operation) 
# that performs addition, subtraction, multiplication, or division based on the operation parameter 
# [ operation parameter can have values operation ‘+’ ‘-’ '*’ ‘/’ ]

# a = int(input("enter 1st number"))
# operation = input("Enter operation (+, -, *, /): ")
# b = int(input("enter 2nd number"))
# def calculator(a, b, operation):

#     if operation == "+":
#         print(a + b)

#     elif operation == "-":
#         print(a - b)

#     elif operation == "*":
#         print(a * b)

#     elif operation == "/":
#         print(a / b)

# calculator(a, b, operation)

#----------------------------------------------------------------

# Q9. Write a function is_prime(n) that returns True if n is a prime number and
# False otherwise, using a loop.

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("enter number: "))

print(is_prime(n))


#----------------------------------------------------------------

# Q10. Let’s create a “Number Guessing Game”. Given a secret number (already
# decided by you), write a program that asks the user to guess it and prints:
# "Too high" if the guess is above the number
# "Too low" if the guess is below
# "Correct" if the guess matches

secret_number = 25

guess = int(input("enter your guess: "))

if guess > secret_number:
    print("Too high")
elif guess < secret_number:
    print("Too low")
else:
    print("Correct")