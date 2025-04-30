# datatypes.py

# why do we need to know the data type of a variable?
# 1. Memory management: Different data types require different amounts of memory.
# 2. Performance: Some operations are faster on certain data types.
# 3. Functionality: Some operations are only available for certain data types.
# 4. Type safety: Knowing the data type helps prevent errors.


#
book = "The Great Gatsby"  # str
author = "F. Scott Fitzgerald"  # str
publication_year = 1925  # int
price = 10.99  # float

list_of_books = ["The Great Gatsby", "To Kill a Mockingbird", "1984"]  # list
list_test = [ 1, 2, 3, 4, 5 ]  # list
list_of_mixed = [1, "The Great Gatsby", 10.99]  # list

# Tuple
coordinates = (10, 20)
print("Tuple:", coordinates)

# Accessing elements
print("X-coordinate:", coordinates[0])

# key, value 
# Dictionary
student = {"name": "Alice", "age": 25, "is_student": True}
print("Dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Adding a key-value pair
student["grade"] = "A"
print("Updated Dictionary:", student)

# Set
unique_numbers = {1, 2, 3, 3, 4}
print("Set:", unique_numbers)

# Adding an element
unique_numbers.add(5)
print("Updated Set:", unique_numbers)

