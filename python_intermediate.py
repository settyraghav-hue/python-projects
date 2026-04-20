# Python Intermediate Concepts
# Classes, File I/O, Error Handling, and More

# 1. CLASSES AND OBJECTS
class FruitBasket:
    def __init__(self, owner):
        self.owner = owner
        self.fruits = []

    def add_fruit(self, fruit):
        self.fruits.append(fruit)
        print(f"Added {fruit} to {self.owner}'s basket")

    def count_fruits(self):
        return len(self.fruits)

    def display_basket(self):
        print(f"{self.owner}'s basket contains: {self.fruits}")

# Create and use a class
basket = FruitBasket("Alice")
basket.add_fruit("apple")
basket.add_fruit("banana")
basket.display_basket()
print(f"Total fruits: {basket.count_fruits()}")

# 2. FILE INPUT/OUTPUT
def save_fruits_to_file(filename, fruits):
    try:
        with open(filename, 'w') as file:
            for fruit in fruits:
                file.write(fruit + '\n')
        print(f"Fruits saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

def load_fruits_from_file(filename):
    try:
        with open(filename, 'r') as file:
            fruits = [line.strip() for line in file.readlines()]
        return fruits
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []

# Save and load fruits
fruits = ["apple", "banana", "orange", "grape"]
save_fruits_to_file("my_fruits.txt", fruits)
loaded_fruits = load_fruits_from_file("my_fruits.txt")
print(f"Loaded fruits: {loaded_fruits}")

# 3. ERROR HANDLING
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input types!")
        return None
    finally:
        print("Division operation completed")

print(divide_numbers(10, 2))  # Works
print(divide_numbers(10, 0))  # ZeroDivisionError
print(divide_numbers(10, "2"))  # TypeError

# 4. LIST COMPREHENSIONS
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Square each number
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Create dictionary from list
fruit_dict = {fruit: len(fruit) for fruit in fruits}
print(f"Fruit lengths: {fruit_dict}")

# 5. LAMBDA FUNCTIONS
# Short anonymous functions
square = lambda x: x**2
print(f"5 squared: {square(5)}")

# Sort with lambda
fruits_sorted = sorted(fruits, key=lambda x: len(x))
print(f"Fruits sorted by length: {fruits_sorted}")

# Filter with lambda
long_fruits = list(filter(lambda x: len(x) > 5, fruits))
print(f"Fruits with names longer than 5 chars: {long_fruits}")

# 6. MODULES AND IMPORTS
import math
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

from datetime import datetime
now = datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

print("Intermediate Python concepts completed!")