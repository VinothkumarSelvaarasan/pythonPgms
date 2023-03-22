b = "Hellof, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, orWld!"
print(b[-5:-2])


a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())


a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
b = a.split(",")
print(b)


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))