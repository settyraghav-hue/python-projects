# This program teaches list creating, appending and display
fruits = ["apple","banana", "orange"]
print(f"First fruit: {fruits[0]}")
fruits.append("grape")
print(f"Fruits : {fruits}")

for fruit in fruits:
	print(f" - {fruit}")

no_fruits=len(fruits) # Gets the number of arrays in the list

print(f"Total number of fruits are {no_fruits}")
print(f"The list of fruits are as follows:")

# For Loop syntax
for i in range(no_fruits):
	print(f"{i+1}. Fruit is {fruits[i-1]}")

# Now we are moving to functions
def pick_fruit(fruitnum):
	fruitnum = input("Enter a fruit number you like : ")
	return fruitnum 

fruitnum = 0
choice = pick_fruit(fruitnum)
print(f"Choice entered is {choice}")
print(f"You like the {fruits[int(choice)]} fruit")
