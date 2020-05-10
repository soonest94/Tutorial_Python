# animal package
# dog, cat modules; can say "hi"
print("tmp_01")

from animal import dog          # get dog module from animal package
from animal import cat          # get cat module from animal package

d = dog.Dog()                   # instance from "Dog" class in "dog" module
d.hi()

c = cat.Cat()
c.hi()


# another way to get package
print("\ntmp_02")

from animal import *            # get all modules from animal package

d = Dog()
c = Cat()

d.hi()
c.hi()
