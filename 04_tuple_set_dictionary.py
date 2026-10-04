# Tuple operations
t = (10, 20, 30, 40)
print("Tuple element:", t[1])

# Set operations
s = {1, 2, 3, 4}
s.add(5)
s.remove(2)
print("Set:", s)

# Dictionary operations
student = {"name": "Amit", "age": 20, "marks": 85}

# Accessing values
print("Name:", student["name"])

# Updating values
student["marks"] = 90

# Adding new key
student["city"] = "Nagpur"

# Deleting key
del student["age"]

print("Updated Dictionary:", student)

# Built-in functions
print("Dictionary keys:", student.keys())
print("Dictionary values:", student.values())
print("Dictionary items:", student.items())
