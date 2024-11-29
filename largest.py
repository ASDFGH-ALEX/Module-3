'''
Author:Alex
Date:29-11-2024
Description:Write a Python program that takes two numbers as input from the user
and prints the larger of the two numbers. If both numbers are equal,
print "The numbers are equal."
'''
num_1=int(input("Enter the first number"))
num_2=int(input("Enter the second number"))
if num_1>num_2:
    print(num_1,"is greater than ",num_2)
elif num_2>num_1:
    print(num_2 ,"is greater than ",num_1)
else:
    print("The number are equal")