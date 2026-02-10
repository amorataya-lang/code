# Python Lists
x = 42
print(x)
print(type(x))

# re-assign the variable 'x' to be a list
print('re-assign the variable "x" to now be a list')
x = [1, 3, 5, 23, 9, 14, 42]
print(x)
print(type(x))

# Creating a list of mixed Type objects
print('Creating a list of mixted Type objects')
x = ['fName', 'lName', 25, True, 4.2]
print('x is now a list of mixed objects')
print(x)
print(type(x))

# Add more hard coded items to your list
print('Add more hard coded items to your list')
x.append('bob')
x.append(67)
x.append(42)
x.append('hi')
print(x)
print(type(x))

# Indexing a List
print("Let's Index the list")
print(x[4])
print(type(x[4]))
y = x[2]
print(y)
print(type(y))
