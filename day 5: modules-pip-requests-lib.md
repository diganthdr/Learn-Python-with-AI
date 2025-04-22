
# 📦 Python Modules, pip & Requests Library

---

## 🧠 What You Learned

### 1. **What is a Module?**
A module is a file containing Python code (functions, classes, or variables) that can be imported and reused.

**Example:**
```python
import math
print(math.sqrt(16))
```

You can create your own module too! Just create a `.py` file and import it.

---

### 2. **Installing Packages with pip**

**pip** is the Python package installer.

- To install a package:
```bash
pip install package-name
```

- Example:
```bash
pip install requests
```

- To list installed packages:
```bash
pip list
```

---

### 3. **The `requests` Library**

Used to send HTTP requests easily.

**Example 1: Simple GET Request**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
```

**Example 2: Handling Query Parameters**
```python
payload = {"q": "python"}
res = requests.get("https://httpbin.org/get", params=payload)
print(res.url)
```

---

## ✅ Assignments

### 🧪 Assignment 1: Create and Import Your Own Module
1. Create a Python file `myutils.py`.
2. Write a function `def greet(name):` that returns `"Hello, <name>!"`
3. In another file, import and use the function:
```python
from myutils import greet
print(greet("Alice"))
```

---

### 🧪 Assignment 2: Use the `requests` Library
1. Write a script that sends a GET request to:
   ```
   https://api.coindesk.com/v1/bpi/currentprice.json
   ```
2. Print the current Bitcoin price in USD.

Bonus: Format the output as:
```
Bitcoin Price: $<value>
```

---

### 🧪 Assignment 3: Install and Use an External Library
1. Pick any library from [https://pypi.org](https://pypi.org).
2. Install it using `pip install`.
3. Write a small demo program using that library.

---

Happy Coding! 🚀
