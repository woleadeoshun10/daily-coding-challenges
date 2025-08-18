1. What is a Hashmap?

A hashmap is a data structure that stores data as key → value pairs.
Think of it like a real dictionary:

Word = key

Meaning = value

Example in Python:

student = {
    "name": "Alex",
    "age": 21,
    "course": "Computer Science"
}
print(student["name"])   # Alex
print(student["age"])    # 21

2. Why Hashmaps?

Hashmaps are 🔑 in interviews because:

They let you find things super fast (almost O(1) time).

Perfect for problems where you need to count, lookup, or track elements.

3. Basic Operations
# Create hashmap
my_map = {}

# Add key-value pairs
my_map["apple"] = 5
my_map["banana"] = 3

# Get a value
print(my_map["apple"])   # 5

# Update a value
my_map["apple"] = 10

# Check if a key exists
if "banana" in my_map:
    print("Banana is here!")

# Loop through hashmap
for fruit, qty in my_map.items():
    print(fruit, qty)

# Delete a key
del my_map["banana"]
