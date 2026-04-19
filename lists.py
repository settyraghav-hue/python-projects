# This program teaches list creating, appending and display
fruits = ["apple","banana", "orange"]
print(f"First fruit: {fruits[0]}")
fruits.append("grape")
print(f"Fruits : {fruits}")

for fruit in fruits:
	print(f" - {fruit}")

no_fruits=len(fruits)

print(f"Total number of fruits are {no_fruits}")
print(f"The list of fruits are as follows:")

for i in range(no_fruits):
	print(f"{i+1}. Fruit is {fruits[i-1]}")
