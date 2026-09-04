"""
Simple Alarm Clock

This program:
    1. Takes an alarm time from the user.
    2. Continuously checks the current time.
    3. When the current time matches the alarm time,
       it plays an MP3 file.
"""


import time
import datetime
import pygame  # Install pygame if you haven't already.


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    # Path to the MP3 file.
    sound_file = "/home/arun/Documents/python_2026/013_date_time/sony_ericsson_official.mp3"

    is_running = True

    while is_running:

        # Get the current time in HH:MM:SS format.
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(current_time)

        # Check whether the current time matches the alarm time.
        if current_time == alarm_time:
            print("WAKE UP!!!!")

            # Initialize pygame's music player.
            pygame.mixer.init()

            # Load the MP3 file.
            pygame.mixer.music.load(sound_file)

            # Start playing the MP3.
            pygame.mixer.music.play()

            # Keep the program running until the music finishes.
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        # Check the time again after 1 second.
        time.sleep(1)


if __name__ == "__main__":

    # Get the alarm time from the user.
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")

    set_alarm(alarm_time)


"""
HOW IT WORKS
------------

Example:

    Enter the alarm time (HH:MM:SS): 18:30:00


The program continuously gets the current time:

    18:29:57
    18:29:58
    18:29:59
    18:30:00

When:

    current_time == alarm_time

the alarm starts playing.


IMPORTANT
---------

strftime("%H:%M:%S")

converts the current time into a string.

For example:

    18:30:00


time.sleep(1)

pauses the program for 1 second.

pygame.mixer.music.play()

starts playing the MP3.


The inner while loop:

    while pygame.mixer.music.get_busy():
        time.sleep(1)

keeps the program running until the MP3 finishes playing.


The outer while loop checks the current time
until the alarm time is reached.
"""