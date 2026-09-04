"""
Working with Date and Time

Python's datetime module is used to work with:

    Date
    Time
    Date and Time
    Formatting
    Comparing dates and times
"""


import datetime


# ===========================================================
# ---------- Date -------------------------------------------
# ===========================================================

# Create a specific date.
date = datetime.date(2026, 7, 23)

print(date)


# Get today's date.
today = datetime.date.today()

print(today)


# ===========================================================
# ---------- Time -------------------------------------------
# ===========================================================

# Create a specific time.
# Arguments: hour, minute, second
time = datetime.time(11, 35, 0)

print(time)


# Get the current date and time.
now = datetime.datetime.now()

print(now)


# Format the date and time into a readable string.
formatted_time = now.strftime("%H : %M : %S %d-%m-%Y")

print(formatted_time)


# ===========================================================
# ---------- Comparing Date and Time -----------------------
# ===========================================================

target_datetime = datetime.datetime(2030, 1, 26, 12, 30, 10)

current_datetime = datetime.datetime.now()


# Compare two datetime objects.
if target_datetime < current_datetime:
    print("Target date has passed!")
else:
    print("Target date has NOT passed!")


"""
IMPORTANT
---------

datetime.date
    → Used when we only need a date.

    Example:
        2026-07-23


datetime.time
    → Used when we only need a time.

    Example:
        11:35:00


datetime.datetime
    → Used when we need both date and time.

    Example:
        2026-07-23 11:35:00


datetime.date.today()
    → Gets today's date.


datetime.datetime.now()
    → Gets the current date and time.


strftime()
    → Converts a date/time into a formatted string.

Example:

    now.strftime("%H : %M : %S %d-%m-%Y")


Some common format codes:

    %H → Hour (24-hour format)
    %M → Minute
    %S → Second

    %d → Day
    %m → Month
    %Y → Year


Example:

    18 : 40 : 25 03-09-2026


Date/time objects can also be compared:

    target_datetime < current_datetime

    target_datetime > current_datetime

    target_datetime == current_datetime


This is useful for things like:

    - Checking whether a deadline has passed
    - Checking an expiry date
    - Comparing appointment times
    - Creating timers and reminders
"""