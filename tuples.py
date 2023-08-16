thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
z = ("pine apple",)
thistuple += y
thistuple += z
print(thistuple)

# getting values in to variables
fruits = ("apple", "banana", "cherry")
#variables are green, yellow and red etc
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)