"""
telephone_number.py
Author: ITP 150 Franco Pisano
Date: March 16, 2026
This script uses Python string slicing and concatenation and if structures to 
check a phone number to see if it is formatted like this: (703)123-4567
If it is formatted as (703)123-4567, then we unformat it to look like this: 
7031234567. If it is formatted like this: 7031234567, then we format it to look like 
this: (703)123-4567.
"""

# These constants hold the lengths of formatted and unformatted phone numbers.
# Constants are in all caps.
FORMATTED_LENGTH = 13
UNFORMATTED_LENGTH = 10

valid = True # Flag to indicate a valid format.
print("Please enter the telephone number.: \
In this format: (xxx)xxx-xxxx:")
telephone = input()

# Determine if the numner is properly formatted.
if (len(telephone) == FORMATTED_LENGTH and \
    telephone[0] == "(" and \
    telephone[4] == ")" and \
    telephone[8] == "-"):
    valid = True
    print("Great! Telephone number", telephone, 
          "is a properly formatted telephone number.")
else: 
    valid = False
    print("Yikes, this phone number", telephone, 
          "is not properly formatted.")
    
# Accept telephone number as this (xxx)xxx-xxxx and return as xxxxxxxxxx.
if valid:
    area_code = telephone[1: 4:] # 1 is inclusive, 4 is exclusive.
    three_digit_prefix = telephone[5: 8:] # 5 is inclusive, 8 is exclusive.
    line_number = telephone[9: 13:] # 9 is inclusive, 13 is exclusive.
    unformatted_telephone = area_code + three_digit_prefix + line_number
    print("Telephone number input is now unformatted as : " + 
          unformatted_telephone)

# Accept telephone number as this xxxxxxxxxx and return as (xxx)xxx-xxxx.
if not valid:
    area_code = telephone[0: 3:] # 0 is inclusive, 3 is exclusive.
    three_digit_prefix = telephone[3: 6:] # 3 is inclusive, 6 is exclusive.
    line_number = telephone[6: 10:] # 6 is inclusive, 10 is exclusive.
    formatted_telephone = "(" + area_code + ")" + three_digit_prefix + \
        "-" + line_number
    print("Telephone number input is now formatted as : " + formatted_telephone)
