
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " is barking")
        print(self.name + " age is " + str(self.age))

dog1 = Dog("Buddy", 3)
dog1.bark()


