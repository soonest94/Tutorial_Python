########## counting fruits program ##########

fruit = ["apple", "apple", "banana", "banana", "berry", "kiwi", "peach", "peach", "peach"]

d = {}

for f in fruit:
    if f in d:                  # Is there the key(ex. "apple") in the dictionary(d)?
        d[f] = d[f] + 1         # If the key is in, count it.
    else:
        d[f] = 1                # If the key is not in, add the key in the dictionary and count it.

print(d)
