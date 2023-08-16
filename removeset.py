thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # order is not always correct and it will change randomly

thisset = {"apple", "banana", "cherry"}
thisset.discard("apple")
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # pop removes randomly  removed item goes in to x
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

  set1 = {"a", "b", "c"}    #union
  set2 = {1, 2, 3}
  set3 = set1.union(set2)
  print(set3)

  set1 = {"a", "b", "c"}  #insert two in one
  set2 = {1, 2, 3}
  set1.update(set2)
  print(set1)

  x = {"apple", "banana", "cherry"}    # in both the sets intersection
  y = {"google", "microsoft", "apple"}
  x.intersection_update(y)
  print(x)

  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"} # method will return a new set, that only contains the items that are present in both sets.
  z = x.intersection(y)
  print(z)

  x = {"apple", "banana", "cherry"}
  y = {"google", "microsoft", "apple"}   #method will keep only the elements that are NOT present in both sets.
  x.symmetric_difference_update(y)
  print(x)



  x = {"apple", "banana", "cherry", True}  #Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
  y = {"google", 1, "apple", 2}  # also apple is duplicate gone
  z = x.symmetric_difference(y)
  print(z)