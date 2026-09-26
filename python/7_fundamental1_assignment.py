# Q1 :- Write a program that asks the user for their name and age, then prints a sentence like: 
# "Hello Shradha, you are 21 years old!"

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print("hello",name, "you are", age, "years old!")

#-------------------------------------------------------

#Q2 Take two numbers as input from the user and print their
# sum, difference, product, and quotien

# num1 = int(input("Enter your num1: "))
# num2 = int(input("Enter your num2: "))

# sum = num1 + num2
# difference = num1 - num2
# product = num1 * num2
# quotien = num1 / num2

# print(sum, difference, product,quotien)

#-------------------------------------------------------

#Q3 Ask the user to enter two integers and one float. Convert them all to floats and print their average.

# num1 = int(input("Enter your num1: "))
# num2 = int(input("Enter your num2: "))
# num3 = float(input("Enter your num3: "))

# new1 = float(num1)
# new2 = float(num2)
# new3 = num3

# print((new1 + new2 + new3)/3)

#-------------------------------------------------------

#Q4 The user enters a string containing a number (e.g."45"). Convert it to
# an integer
# • a float
# • a string again
# Print all three values with their types.

# num1 = input("Enter your num1: ")

# print("your enter number in different type: ",int(num1), "it's type is:", type(int(num1)), float(num1), "it's type is: ", type(float(num1)), num1, "it's type is: ", type(num1))

#-------------------------------------------------------

# Q5 Evaluate and print the result of the following expression:
# x = 10 + 3 * 2 ** 2 . Based on what you learnt in the lecture explain why the output is what it is.
# x = 10 + 3 * 2 ** 2
# print(x)
# ** is evaluated first, then *, then +: 10 + 3 * 4 = 22.

#-------------------------------------------------------

# Q6 Write a program to SWAP values of two numbers entered by the user.

# num1 = input("Enter your num1: ")
# num2 = input("Enter your num2: ")

# num1, num2 = num2, num1

# print("your changed values are: ",num1,num2)

#-------------------------------------------------------

# Q7 Ask the user for a temperature in Celsius (string input). Convert it to FLOAT ,
# then calculate and print temperature in Fahrenheit.
# Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32

# CelsiusTemp = float(input("Enter your temp in Celsius : "))

# FahrenheitTemp = ((CelsiusTemp * (9/5)) + 32)
# print(FahrenheitTemp)
#-------------------------------------------------------

# Q8 Take the radius ( ) as user input and print the area.
# Use the formula: Area = π * r**2 (value of π = 3.14)

# r = int(input("Enter your radius: "))
# pi = 3.14
# print(pi * r ** 2)

#-------------------------------------------------------

# Q9 Ask the user for: Principal (P), Rate (R), Time (T). Convert all to FLOAT and
# compute simple interest: SI = (P ∗ R ∗ T )/100

# P = float(input("Enter your P: "))
# R = float(input("Enter your R: "))
# T = float(input("Enter your T: "))
# SI = (P * R * T )/100
# print(SI)


# Q10 Take a decimal number as input (like 45.78 ) and output its: 
# • integer part - 45
# • fractional part - .78

num1 = float(input("Enter your float: "))

integer_part = int(num1)
fractional_part = num1 - integer_part
print("integer part -", integer_part, "fractional part - ",fractional_part)




