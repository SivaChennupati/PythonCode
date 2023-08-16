fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
#Based on a list of fruits, you want a new list, containing only the fruits containes the letter "a" in the name.
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "e" in x]  # contains e

print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["apple", "banana", "cherry"]  # using copy
newlist = thislist.copy()
print(newlist)

thislist = ["apple1", "banana2", "cherry3"]
newlist1 = list(thislist)
print(newlist1)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

