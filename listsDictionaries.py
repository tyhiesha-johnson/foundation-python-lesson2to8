# Working with Lists

fruits = ["apple", "banana", "cherry"]

# Accessing items
print("First fruit:", fruits[0])

# Adding an item
fruits.append("orange")
print("After adding orange:", fruits)

# Removing an item
fruits.remove("banana")
print("After removing banana:", fruits)

# Looping through a list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)
