def greet(name):
    return "Hello, " + name + "!"

print(greet("Bob"))

fruits = ["apple", "banana", "orange"]
print(fruits[0])
fruits.append("grape")
print(len(fruits))

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person["name"])
person["occupation"] = "Engineer"
print(person)


class Dog:  # class dog has method bark and has self as array and array has two properties name and age
    age: object

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):   # in this bark we call self array and can pass parameters while instatiting the method
        print(self.name + " is barking")
        print(self.name + " age is " + self.age)

dog1 = Dog("Buddy", 3)
dog1.bark()

dog2 = Dog("Raja", 5)
dog2.bark()

