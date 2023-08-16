b = "Hello, World!"
print(b[2:5])  # from 3nd to 5  since index start from 0 --0 1 2 3 4 5
print(b[:12])  # from 0 to 5
print(b[:9])  # from 2nd to 5

q = "Hello, World!"
print(q[:5])  #startig five

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())
a = "                       Hello, World! "
print(a.strip()) # returns "Hello, World!"   remove spaces

age = " Male "
txt = "My name is John, and I am {}"   # in the bracket the parameter goes
print(txt.format(age))


age = 36
txt = "My name is John, and I am {}"   # in the bracket the parameter goes
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3  # 0
itemno = 567  # 1
price = 49.95  # 2
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))