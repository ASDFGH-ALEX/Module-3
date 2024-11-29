'''
Author:Alex
Date:29-11-2024
Description:Write a Python program that takes a single character as input from the
user and checks if it is a vowel or a consonant. If the input is not an
alphabetic character, print "Invalid input."
'''
char_1=input("Enter the character")
if char_1.isalpha():
    if char_1 in 'AEIOU aeiou':
        print("The character entered is a vowel")
    else:
        print("The character entered is a consonant")
else:
    print("Invalid input")