# Python Basics Tutorial
# This is a comment - lines starting with # are ignored

# 1. Variables - storing data
name = "Your Name"  # String (text)
age = 25           # Integer (whole number)
height = 5.9       # Float (decimal number)
is_student = True  # Boolean (True/False)

# 2. Printing output
print("Hello, World!")
print(f"My name is {name} and I'm {age} years old")

# 3. Basic math
x = 10
y = 3
print(f"Addition: {x + y}")      # 13
print(f"Subtraction: {x - y}")   # 7
print(f"Multiplication: {x * y}") # 30
print(f"Division: {x / y}")      # 3.333...
print(f"Integer division: {x // y}") # 3
print(f"Modulus (remainder): {x % y}") # 1
print(f"Power: {x ** y}")        # 1000

# 4. Lists - collections of items
fruits = ["apple", "banana", "orange"]
print(f"First fruit: {fruits[0]}")  # apple
fruits.append("grape")  # Add item
print(f"Fruits: {fruits}")

# 5. Conditional statements
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# 6. Loops
print("Counting to 5:")
for i in range(1, 6):  # 1 to 5
    print(i)

print("Fruits in list:")
for fruit in fruits:
    print(f"- {fruit}")

# 7. Functions - reusable code
def greet_person(person_name):
    return f"Hello, {person_name}!"

message = greet_person("Alice")
print(message)

# 8. Input from user
# user_name = input("What's your name? ")
# print(f"Nice to meet you, {user_name}!")

print("Python basics completed!")