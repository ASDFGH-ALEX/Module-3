'''
Author:Alex
Date:29-11-2024
Description:Write a Python program to calculate the sum of the first N natural
numbers using a for loop. The user will input N.
'''
num=int(input("Enter the number: "))
total_sum=0
for i in range(1,num+1):
    total_sum+=i
print("The sum of first N natural nuber is",total_sum)