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


############### inheritance ###############
print("\n inheritance")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("I am " + self.name + " and I am " + str(self.age) + "years old.")

class Police(Person):
    def arrest(self, to_arrest):
        print("You are under arrest, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("What should I do next? Ah, I'm gonna make " + to_program)

Parker = Person("Peter", 20)
Romanoff = Police("Natasha", 21)
Strange = Programmer("Steve", 22)

Parker.introduce()
Romanoff.introduce()            # Even Romanoff is in Police class, we can use func in Person class cuz Police is belong to Person so it inherited all funcs from Person class.
Romanoff.arrest("Parker")
Strange.introduce()
Strange.program("e-mail client")
