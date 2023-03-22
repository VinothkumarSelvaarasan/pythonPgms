x="vinoth"
x=10
print("Welcome to Printing Variable ",x)

#Another Way to assign the value
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value assign to multiple value
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking values
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#output
x = 5
y = "John"
print(x, y)

"""
when u concat string and number together u need to use ,
if u try to use + for concat string and number it through an error
"""


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
