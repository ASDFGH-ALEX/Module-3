'''
Author:Alex
Date:29-11-2024
Description:► Write a Python program that takes a year as input and checks if the year
is a leap year.
► If the year is divisible by 400, it is a leap year.
► If the year is divisible by 100 but not 400, it is not a leap year.
► If the year is divisible by 4 but not 100, it is a leap year
'''
yrs=int(input("Enter the year"))
if yrs%400==0:
    print("It is a leap year")
elif yrs%100==0 and yrs%400!=0:
    print("It is not a leap year")
elif yrs%4==0 and yrs%100!=0:
    print("It is a leap year")
else:
    print("Invalid entry")