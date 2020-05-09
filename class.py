############### class 101 ###############
# basic form
print("basic form")
class person:
    name = "Tony"

    def say_hello(self):
        print("Hello! I am " + self.name)

p = person()
p.say_hello()

# basic usage of class
print("\n usage of class")
print(" form_01")
class Person:
    def __init__(self, name):           # init means initialize.
        self.name = name

    def say_hello(self):
        print("Hello! I am " + self.name)

Stark = Person("Tony")
Rogers = Person("Steve")
Banner = Person("Bruce")

Stark.say_hello()
Rogers.say_hello()
Banner.say_hello()

print("\n form_02")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("Hello! " + to_name + ". I am " + self.name)

    def introduce(self):
        print("I am " + self.name + " and I am " + str(self.age) + "years old.")

Stark = Person("Tony", 20)
Rogers = Person("Steve", 21)
Banner = Person("Bruce", 22)

Stark.say_hello("Pepper")
Rogers.say_hello("Peggy")
Banner.say_hello("Betty")

Stark.introduce()
