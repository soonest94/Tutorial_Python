# this file make this folder to package
# and also means, all files(modules) in same folders gonna be a parts of that package

from .dog import Dog            # .     <- get the class name "Dog" from dog.py in THIS folder
from .cat import Cat            # .     <- get the class name "Cat" from cat.py in THIS folder
                                # from .cat import *    <- get all codes in cat.py module

