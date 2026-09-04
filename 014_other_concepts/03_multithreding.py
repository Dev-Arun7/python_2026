"""
Multithreading

Multithreading allows multiple tasks to run concurrently.

It is especially useful for I/O-bound tasks such as:

    - Reading files
    - Fetching data from APIs
    - Downloading files
    - Waiting for network responses
"""


import threading
import time


def walk_dog(first, last):
    time.sleep(8)
    print(f"You finished walking {first} {last}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


# Create a thread for each task.
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Do"))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)


# Start all three tasks.
chore1.start()
chore2.start()
chore3.start()


# Wait for all threads to finish.
chore1.join()
chore2.join()
chore3.join()


print("All chores are finished!")


"""
HOW IT WORKS
------------

Without multithreading:

    walk_dog()
        ↓
    Wait 8 seconds
        ↓
    take_out_trash()
        ↓
    Wait 2 seconds
        ↓
    get_mail()
        ↓
    Wait 4 seconds

Total time ≈ 14 seconds.


With multithreading:

    walk_dog()       → 8 seconds
    take_out_trash() → 2 seconds
    get_mail()       → 4 seconds

All three tasks can run at the same time.

Total time ≈ 8 seconds.


IMPORTANT
---------

threading.Thread()
    → Creates a thread for a task.


target=
    → Specifies which function the thread should run.


args=
    → Passes arguments to the target function.

    Example:

    args=("Scooby", "Do")


start()
    → Starts the thread.


join()
    → Waits for the thread to finish.

The program does not print:

    "All chores are finished!"

until all three threads have completed.


Simple flow:

    Create threads
          ↓
       start()
          ↓
    Tasks run concurrently
          ↓
        join()
          ↓
    Wait for all tasks
          ↓
    Program continues
"""