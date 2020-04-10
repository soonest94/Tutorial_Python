x = True
y = False

print(x)
print(y)

if 2 > 1:
    print("2 is bigger than 1.")

if 1 > 2:
    print("1 is bigger than 2.")

if 1 > 0 and 2 > 1:
    print("1 is bigger than 0 and 2 is bigger than 1.")

if 0 > 0 and 2 > 1:
    print("0 is bigger than 0 and 2 is bigger than 1.")

if 0 > 0 or 2 > 1:
    print("0 is bigger than 0 or 2 is bigger than 1.")


x = 3

if x > 2:
    print("x is bigger than 2.")

if x > 5:
    print("x is bigger than 5.")
elif x == 3:
    print("x is 3.")
else:
    print("x is smaller than 5.")
