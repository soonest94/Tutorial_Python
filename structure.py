#################### list ####################

x = [1, 2, 3, 4]
y = ["hello", "world"]
z = ["hello", 1, 2, 3]

print(x)
print(y)
print(z)

print(x + y)            # possible to add lists.

print(x[0])             # x = [1, 2, 3, 4] means
                        # x[0] = 1, x[1] = 2, x[2] = 3, x[3] = 4

x[3] = 10
print(x)                # possible to change an element in list.


####### advanced tools for list function #######

x = [1, 2, 3, 4]

num_elements = len(x)
print(num_elements)     # show the length of the list


x = [4, 2, 3, 1]

y = sorted(x)           # sorting the list in order; y = [1, 2, 3, 4]
print(y)

z = sum(x)              # add all elements together
print(z)

# loop with list
x = [4, 2, 3, 1]
y = ["hello", "there"]

for n in x:
    print(n)
for c in y:
    print(c)

print(x.index(3))       # find where a element is in list
                        # CAUTION: The position of elements in list starts with 0.
print(y.index("hello"))

print("hello" in y)     # judge the element is in list; TRUE or FALSE

if "hello" in y:
    print("hello exists in the list.")


#################### tuple ####################

x = tuple()
y = ()

print(x)
print(y)                # technically "list" and "tuple" are very similar.


x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, "hello", "there")

print(x)
print(y)
print(z)

print(x + y)
print('a' in y)
print(z.index(1))

# "tuple" adject does not support item assignment.
# this means, it can not change any element in tuple.
# this is the most biggest difference between "list" and "tuple": "list" is mutable and "tuple" is immutable.


################## dictionary ##################

x = dict()
y = {}

print(x)
print(y)                # dictionary is also similar with list and tuple.


x = {
    "name": "Sergio",
    "age": 20,
    }                   # dictionary is composed with "key" and "value".

print(x["name"])        # "name" is a key and "Sergio" is the value for that key.
print(x["age"])         # "age" is a key and "20" is the value for that key.

# "key" is always immutable. this means, "list" can not be a key.

x = {
    0: "Andreo",
    1: "Hola",
    "age": 20,
    }

print(x[0])
print(x[1])
print(x["age"])

print("age" in x)
print("name" in x)

print(x.keys())         # show all keys in a dictionary.
print(x.values())       # show all values in a dictionary.

for key in x:
    print("key: " + str(key))
    print("value: " + str(x[key]))

# dictionary support item assignment.

x[0] = "Berlin"
print(x)

x["Actor"] = "Pedro Alonso"
print(x)
