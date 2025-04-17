
# 🧠 Python Bootcamp Assignment: Mixed Data Types, Conditionals & Loops

## 🎯 Objective
Understand how mixed data types, conditional statements, and loops work in Python — especially when used with nested structures.

---

## 🔧 How to Complete This Assignment
1. Carefully read each code snippet.
2. Modify the code as suggested in comments.
3. Predict the output before running.
4. Observe and note the behavior after execution.
5. Try additional experiments if you're curious!

---

## 🔹 1. Mixed Data Types in Lists

```python
# Original
items = [42, "hello", 3.14, True]
for item in items:
    print(type(item), item)

# Modify:
# a. Add a dictionary and a list into `items`.
# b. Use isinstance() to print only the strings.
```

---

## 🔹 2. Conditional Statements in a Loop

```python
# Original
numbers = [12, 5, 8, 21, 17]
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")

# Modify:
# a. Add an else block to print odd numbers.
# b. Try filtering numbers > 10 using if condition.
```

---

## 🔹 3. Nested List Iteration

```python
# Original
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()

# Modify:
# a. Add a third row.
# b. Print only even numbers.
```

---

## 🔹 4. Dictionary with Mixed Values

```python
# Original
profile = {
    "name": "Alex",
    "skills": ["Python", "ML"],
    "age": 25,
    "active": True
}

for key, value in profile.items():
    print(key, "=>", value)

# Modify:
# a. Add another key-value pair where value is a dictionary.
# b. Check if value is a list, and print each item separately.
```

---

## 🔹 5. List of Dictionaries

```python
# Original
students = [
    {"name": "Riya", "marks": 78},
    {"name": "Arjun", "marks": 92}
]

for student in students:
    if student["marks"] > 80:
        print(student["name"], "is a topper")

# Modify:
# a. Add one more student.
# b. Use elif to print messages for average, good, and excellent.
```

---

## 📝 Optional Table for Observations

| Concept | What I Modified | Prediction | Actual Result | Why It Happened |
|--------|------------------|------------|----------------|------------------|
| Mixed Types | | | | |
| Conditionals | | | | |
| Nested Loop | | | | |
| Dictionary | | | | |
| List of Dicts | | | | |

---

Happy experimenting! 🧪💡 Try breaking the code too — you’ll learn faster!
