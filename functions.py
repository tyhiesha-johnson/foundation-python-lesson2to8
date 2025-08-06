# Basic example of functions in Python
# Functions are reusable blocks of code that perform a specific task.



def greet(name):
    """This function takes a name and prints a greeting."""
    print("Hello,", name + "!")

def add_numbers(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# Calling the functions
greet("Alice")

result = add_numbers(5, 7)
print("The sum is:", result)