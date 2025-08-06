# Basic example of conditional logic in Python
# Conditional logic allows you to execute different code based on certain conditions.

# Set your variable
# This is an integer representing age
age = 20

# Using if-elif-else statements to check conditions
# If age is less than 13, print "You are a child."
# If age is between 13 and 19, print "You are a teenager."
if age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
