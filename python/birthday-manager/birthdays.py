# birthdays.py
# Author: Franco Pisano
# Created: April 2, 2026
# This script allows us to store the names and birthdays for our frieds
# in a Python dictionary where name is the key and their birthday is the value.

import csv
# Constants that represent menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
PRINT = 5
SAVE = 6
QUIT = 7

choice = 0
birthdays = {} # initializing the empty birthdays dictionary

while choice != QUIT:
    print('Friends and their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Print the birthdays')
    print('6. Save the birthdays')
    print('7. Quit the program.')
    print()

    choice = int(input('\nPlease enter your choice from the menu above:\n'))
    print()

    while choice < 1 or choice > 7:
        choice = int(input('Invalid. Please enter a choice from 1 to 7:\n'))

    if choice == LOOK_UP:
        # look up a birthday
        name = input("Enter a friend's name:\n")
        print(birthdays.get(name, 'Not found'))
    elif choice == ADD:
        # add a birthday
        name = input('Enter a name:\n')
        print('Enter the birthday for', name, '\n')
        bday = input()
        print()

        # check to see if the birthday is already in the dictionary
        if name not in birthdays:
            birthdays[name] = bday
        else:
            print('That name already exists.')
    elif choice == CHANGE:
        name = input('Enter a name:\n')
        if name in birthdays:
            bday = input('Enter the new birthday:\n')
            birthdays[name] = bday
        else:
            print(name, ' is not found.')
    elif choice == DELETE:
        name = input('Enter a name:\n')
        if name in birthdays:
            del birthdays[name]
            print('The name and birthday was deleted.')
        else:
            print(name, ' was not found.')
    elif choice == PRINT:
        for key in birthdays:
            print(key, ":", birthdays[key])
        print('---------------------------')
        print()
    elif choice == SAVE:
        try:
            birthdays_file = csv.writer(open('birthdays_file.csv', 'a'))
            for key, val in birthdays.items():
                birthdays_file.writerow([key, val])
        except IOError:
            print('An error occurred when trying to access the file')
        except:
            print('An error occurred.')
    else:
        print('Happy Birthday!')
