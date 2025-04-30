import json

# Load the JSON file
with open("students.json", "r") as file:
    data = json.load(file)





# Access and print the data
for name, details in data["students"].items():
    print(f"Name: {name}")
    print(f"  Age: {details[0]}")
    print(f"  Grade: {details[1]}")
    print(f"  Major: {details[2]}")