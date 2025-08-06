# Importing necessary modules
# Why we import modules?
# Modules allow us to use pre-written code, which saves time and effort.
# They provide additional functionality that can be reused across different programs.
import time
import math
import random

# Using time module to measure how long a task takes
start_time = time.time()

# Example task: calculate square roots of numbers 1 to 5
for i in range(1, 6):
    print(f"Square root of {i} is {math.sqrt(i):.2f}")
    time.sleep(0.5)  # Pause for half a second

end_time = time.time()
elapsed = end_time - start_time
print(f"\nTask completed in {elapsed:.2f} seconds.")

# Using random module to pick a random number
random_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_num}")
