thisset1 = {"apple", "banana", "cherry"}
print(thisset1)
#duplicates ignored
thisset2 = {"apple", "banana", "cherry", "apple"}

print(thisset2)

thisset3 = {"apple", "banana", "cherry"}

for x in thisset3:
  print(x)

  thisset4 = {"apple", "banana", "cherry"}
  print("banana" in thisset4)  # search  true or false

  thisset = {"apple", "banana", "cherry"}
  thisset.add("orange")
  print(thisset)

  thisset = {"apple", "banana", "cherry"}
  tropical = {"pineapple", "mango", "papaya"}
  thisset.update(tropical)
  print(thisset)

  thisset = {"apple", "banana", "cherry"}
  mylist = ["kiwi", "orange"]
  thisset.update(mylist)
  print(thisset)