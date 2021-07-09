#Classes provide a means of bundling data and functionality together.
#Creating a new class creates a new type of object, allowing new instances of that type to be made.
#Each class instance can have attributes attached to it for maintainging its state.
#Class instances can also have methods for modifying its state.

#Class definitions play some neat tricks with namespaces
#   . A namespace is a mapping from names to objects.
#       . Most namespaces are currently implemented as Python dictionaries
#       . Examples of namespace:
#           . the set of built-in names(containing functions such as abs())
#           . the global names in a module

class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, num):
        self.i = num

    def f(self):
        print(self.i)
        return 'hello world'

x = MyClass(4321)
print(x.f())

class Dog:
    name = ""
    tricks = []
    def __init__(self, name):
        self.name = name
        self.tricks = []   #Creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
        return "trick"

    def do_tricks(self):
        print(self.name + "can do:")
        print(self.tricks)
        return "test"

d = Dog("Pickel")
e = Dog("Rocket")
d.add_trick('roll over')
e.add_trick('pop')
d.do_tricks()
e.do_tricks()



