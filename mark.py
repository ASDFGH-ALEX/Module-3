'''
Author:Alex
Date:29-11-2024
Description:Write a Python program that takes a student's marks as input and prints
their grade based on the following criteria:
► Marks >= 90: A
► Marks 80–89: B
► Marks 70–79: C
► Marks 60–69: D
► Marks < 60: F
'''
mark=int(input("Enter the total mark of the student"))
if mark>=90:
    print("Grade is A")
    print("Excellent")
elif mark>80:
    print("Grade is B")
    print("Very Good")
elif mark>70:
    print("Grade id C")
    print("Good")
elif mark>60:
    print("Grade is D")
    print("Average")
elif mark<60:
    print("Grade is F")
    print("Poor Grade")
else:
    print("Invalid Entry")