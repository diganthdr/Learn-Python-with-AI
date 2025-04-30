# Nested dictionary with lists
students = {
    "Alice": [25, "A", "Computer Science"],
    "Bob": [22, "B", "Mathematics"],
    "Charlie": [23, "A", "Physics"]
}

# Iterating through the nested dictionary
for name, details in students.items():
    print(f"Name: {name}")
    print(f"  Age: {details[0]}")
    print(f"  Grade: {details[1]}")
    print(f"  Major: {details[2]}")