"""
temperatures.py
@author: Franco Pisano
Created: March 31, 2026
This script tracks temperatures over a number of days chosen by the user.
We can then calculate descriptive statistics (min, max, average) for
the temperatures entered.
"""

num_days = int(input('How many days do you want to track temperatures?'))
# I added input validation so the user cannot enter a number < 1.
while num_days < 1:
    print('You must enter a number greater than 0. Please try again.')
    num_days = int(input('How many days do you want to track temperatures?'))

# initialize the lists specifying data type and size
dates = [' '] * num_days
lows = [0.0] * num_days
highs = [0.0] * num_days
average_temps = [0.0] * num_days

# The commented lines below were used to verify the size and contents of
# the lists so far, and we see how to use type to determine if we have a list
# or a simple variable like an int, float, or string.
# print(dates)
# print(lows)
# print(highs)
# print(average_temps)
# print(type(dates))
# print(type(num_days))
#
# loop that loads the data into the lists. The user enters the data except
# for average_temps and we calculate that.
# for i in range(0, num_days, 1): 
for i in range(num_days): # This does the same as above but is more concise.
    dates[i] = input('Please enter the date (ex. Mar. 31)')
    print('Please enter the low for', dates[i])
    lows[i] = float(input())
    print('Please enter the high for', dates[i])
    highs[i] = float(input())
    average_temps[i] = (lows[i] + highs[i]) / 2

# uncomment the lines below if you want to see the lists with data so far.
# print(dates)
# print(lows)
# print(highs)
# print(average_temps)

# for loop to print each item in the lists in a columnar format
print('-' * 51)
print(f'{"Dates":8} {"Lows":>10s} {"Highs":>10s} {"Average Temps":>20s}')
# for i in range(0, len(dates), 1):
for i in range(len(dates)): # This does the same as above but is more concise.
    print(f'{dates[i]:8} {lows[i]:10.1f} {highs[i]:10.1f} {average_temps[i]:20.1f}')
print('-' * 51)

# code block for finding lowest low temp and the date it occurred on
lowest_low = min(lows) # min works for single dim list
lowest_low_date = ' '
# for i in range(0, len(lows), 1):
for i in range(len(lows)): # This does the same as above but is more concise.
    if lows[i] == lowest_low:
        lowest_low_date = dates[i]
print('-' * 51)
print(f'{"Lowest Low Temp":30} {lowest_low:20,.1f}')
print(f'{"Lowest Low Date":30} {lowest_low_date:>20s}')
print('-' * 51)

# code block for finding highest high temp and the date it occurred on
highest_high = max(highs)
highest_high_date = ' '
# for i in range(0, len(highs), 1):
for i in range(len(highs)): # This does the same as above but is more concise.
    if highs[i] == highest_high:
        highest_high_date = dates[i]
print('-' * 51)
print(f'{"Highest High Temp":30} {highest_high:20,.1f}')
print(f'{"Highest High Date":30} {highest_high_date:>20s}')
print('-' * 51)

# calculating the average of the average_temps
sum_average_temps = sum(average_temps) # works on single dim lists
average_average_temps = sum_average_temps / len(average_temps)
# this would work too in only 1 line of code
# average_average_temps = sum(average_temps) / len(average_temps)

print('-' * 51)
print(f'{"Average of Average Temps":30} {average_average_temps:20,.1f}')
print('-' * 51)
