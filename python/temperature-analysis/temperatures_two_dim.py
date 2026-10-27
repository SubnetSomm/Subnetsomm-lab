"""
temperatures_two_dim.py
Author: Franco Pisano
Created: March 31, 2026
This script stores information about temperatures recording the dates,
lows, highs, and calculating the average temperature for the date in
a two dimensional list.
"""


# num_days will set the sizes of the lists
num_days = int(input('How many days do you want to track temperatures?'))
COLS = 4
sum_high_temps = 0
HIGH_TEMP = 90

# initializing the lists by datatype and the size via num_days
temperatures = [[0 for col in range(COLS)] for row in range(num_days)]
# print(temperatures) # notice the [[0, 0, 0, 0], ...] to indicate 2 dim list


# loop that loads the values into the dates, lows, highs columns [0, 1, 2]
# within the temperatures list and calculates the values for the
# average temps column which is column 3.
for row in range(0, num_days, 1):
    temperatures[row][0] = input('Please enter the date (ex. Jul. 25):')
    print('Please enter the low temperature for ', temperatures[row][0], ':')
    temperatures[row][1] = float(input())
    print('Please enter the high temperature for ', temperatures[row][0], ':')
    temperatures[row][2] = float(input())
    temperatures[row][3] = (temperatures[row][1] + temperatures[row][2]) / 2
# print(temperatures) # print to see the data then comment or delete

print('-' * 55)
# loop that prints the details more prettily from the lists
print(f'{"Dates":10} {"Lows":>10} {"Highs":>10} {"Average Temps":>20}')
for row in range(0, num_days, 1):
    print(f'{temperatures[row][0]:<10s} {temperatures[row][1]:>10.1f} \
{temperatures[row][2]:>10.1f} {temperatures[row][3]:>20.1f}')
print('-' * 55)
#
# algorithm to find the lowest low and its date
lowest_low = temperatures[0][1] # use min() only with single dim list
lowest_low_date = temperatures[0][0]

for row in range(0, num_days, 1):
    if temperatures[row][1] < lowest_low:
        lowest_low = temperatures[row][1]
        lowest_low_date = temperatures[row][0]
print('-' * 55)
print(f'{"Lowest Low":30s} {lowest_low:>22.1f}')
print(f'{"Lowest Low Date":30s} {lowest_low_date:>22s}')
#
# algorithm to find the highest high and its date
highest_high = temperatures[0][2]
highest_high_date = temperatures[0][0]

for row in range(0, num_days, 1):
    if temperatures[row][2] > highest_high:
        highest_high = temperatures[row][2]
        highest_high_date = temperatures[row][0]
print(f'{"Highest High":30s} {highest_high:>22.1f}')
print(f'{"Highest High Date":30s} {highest_high_date:>22s}')
#
# code to calculate the average of the highs
for row in range(0, num_days, 1):
    sum_high_temps = sum_high_temps + temperatures[row][2]

average_highs = sum_high_temps / len(temperatures) # use sum() for a single dim list
print(f'{"Average Highs":30s} {average_highs:>22.1f}')

# algorithm to print each day where high >= 90 which is value
# stored in HIGH_TEMP. When entering test data, enter at least 1
# day with an 90 as the high
for row in range(0, num_days, 1):
    if temperatures[row][2] >= HIGH_TEMP:
        print('The high temp exceeded', HIGH_TEMP, 'on',
              temperatures[row][0], 'recorded at', temperatures[row][2], '.')
print('-' * 55)
