# Creating a list
numbers = [10, 20, 30, 40, 50]
# Accessing values
print("First element:", numbers[0])
print("Last element:", numbers[-1])
# Updating list
numbers[2] = 35
print("Updated list:", numbers)
# Adding elements
numbers.append(60)
numbers.insert(1, 15)
print("After insertion:", numbers)
# Deleting elements
numbers.remove(40)
del numbers[0]
print("After deletion:", numbers)
# Built-in functions
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
numbers.sort()
print("Sorted list:", numbers)
