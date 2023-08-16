tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)  #getting 8th value  position  index

print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 8 )

x = thistuple.count(5)  # no of occurances
y = thistuple.count(8)  # no of occurances

print(x)
print(y)