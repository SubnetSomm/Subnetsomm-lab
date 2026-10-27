"""
seconds_converter.py
Author: Franco Pisano
Date Created: Feb 10, 2026
This script prompts the user to input total seconds, and then
calculates and displays the hours, minutes, and seconds for the number
of seconds entered by the user. It requires the use of floor and
modulo division operators in python.
"""

SECONDS_IN_HOUR = 3600 # 60 seconds * 60 minutes
SECONDS_IN_MINUTE = 60 # 60 Seconds in 1 minute

# Get a numner of seconds from the user
print('Please enter total seconds to convert to hours, minutes, and seconds')
total_seconds = int(input())

# Calculate the whole numner of hours within the total_seconds.
hours = total_seconds // SECONDS_IN_HOUR

# Calculate the seconds remaining after whole hours are removed.
seconds_remaining_after_hours = total_seconds % SECONDS_IN_HOUR

# Calculate the minutes remaining within the total_seconds
minutes = seconds_remaining_after_hours // SECONDS_IN_MINUTE

# Calculate the seconds remaining after hours and minutes are removed.
seconds = total_seconds % SECONDS_IN_MINUTE

# Display the results
print('Hours: ', hours)
print('Minutes: ', minutes)
print('Seconds: ', seconds)
