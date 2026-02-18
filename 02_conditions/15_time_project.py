# --------------------------------------------------
# TIME MODULE PRACTICE — SINGLE SCRIPT
# Practical examples using time + loops
# --------------------------------------------------

import time


# --------------------------------------------------
# Example 1: Loading animation
# Shows simple progress dots
# --------------------------------------------------

print("Loading", end="")

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(1)

print("\nLoaded successfully ✅")


# --------------------------------------------------
# Example 2: Countdown with message
# --------------------------------------------------

print("\nStarting countdown...\n")

for i in range(5, 0, -1):
    print("Starting in", i)
    time.sleep(1)

print("Started 🚀")


# --------------------------------------------------
# Example 3: Simple progress counter
# --------------------------------------------------

print("\nProcessing task...\n")

for i in range(1, 6):
    print(f"Step {i} completed")
    time.sleep(1)

print("Task completed ✅")


# --------------------------------------------------
# Example 4: Digital timer (MM:SS format)
# --------------------------------------------------

total_seconds = 10

print("\nDigital timer running...\n")

for x in range(total_seconds, 0, -1):

    seconds = x % 60
    minutes = x // 60

    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Timer finished ⏰")


# --------------------------------------------------
# Example 5: Simple stopwatch simulation (fixed duration)
# --------------------------------------------------

print("\nStopwatch simulation\n")

seconds = 0

for i in range(5):
    print("Elapsed:", seconds, "seconds")
    time.sleep(1)
    seconds += 1

print("Stopwatch ended ⏱️")


# --------------------------------------------------
# END OF SCRIPT
# --------------------------------------------------
