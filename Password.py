'''
Author:Alex
Date:29-11-2024
Description:► Write a Python program that checks the strength of a password entered
by the user. The program should categorize the password as:
► "Weak" if it is less than 6 characters.
► "Medium" if it is between 6 and 10 characters.
► "Strong" if it is more than 10 characters.
'''
str_1=input("Enter the password of the user")
str_2=len(str_1)
if str_2<6:
    print("Weak password")
elif str_2<=10:
    print("Medium password")
else:
    print("Strong password")
