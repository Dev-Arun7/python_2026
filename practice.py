import time

print("Loading", end="")

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(1)

print("\nLoaded successfully ✅")