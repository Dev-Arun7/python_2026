# --------------------------------------------------
# TIME MODULE PRACTICE
# Learn how to pause program execution using time.sleep()
# --------------------------------------------------

import time


# --------------------------------------------------
# Example 1: Simple delay
# Program waits 3 seconds before printing message
# --------------------------------------------------

print("Waiting for 3 seconds...")
time.sleep(3)
print("3 seconds are over ⏰")


# --------------------------------------------------
# Example 2: User controlled delay
# User enters how many seconds to wait
# --------------------------------------------------

my_time = int(input("\nEnter time in seconds: "))
time.sleep(my_time)
print("Time up ⏰")


# --------------------------------------------------
# Example 3: Count up timer
# Prints numbers from 1 to entered time
# --------------------------------------------------

my_time = int(input("\nEnter time for count up: "))

for x in range(1, my_time + 1):   # +1 to include last number
    time.sleep(1)
    print(x)

print("Time up ⏰")


# --------------------------------------------------
# Example 4: Countdown timer
# Counts down to zero
# --------------------------------------------------

my_time = int(input("\nEnter time for countdown: "))

for x in range(my_time, 0, -1):
    time.sleep(1)
    print(x)

print("Time up ⏰")


# --------------------------------------------------
# Example 5: Digital clock countdown (HH:MM:SS)
# Converts seconds into hours, minutes, seconds
# --------------------------------------------------

my_time = int(input("\nEnter time in seconds for digital clock: "))

for x in range(my_time, 0, -1):

    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    # Format with leading zeros (02 means always show 2 digits)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)

print("Time's up ⏰")
