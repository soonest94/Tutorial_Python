# for loop

print("########## for loop ##########")
for i in range(3):
    print(i)
    print("Berlin: Como estas?")
    print("Profesor: Bien, bien. Y tu?")


# while loop

print("\n ########## while loop ##########")
i = 0
while i < 3:
    print(i)
    print("Berlin: Hola.")
    print("Profesor: Buenas tardes.")
    i = i + 1


# Infinite loop

print("\n ######### infinite loop #########")
i = 0
while True:
    print(i)
    print("Vale, vale, vale!")
    i = i + 1

    if i > 2:
        break


# "break" and "continue"

print("\n ####### break and continue #######")
for i in range(3):
    print(i)
    print("Jajaja")

    if i == 1:
        continue

    print("Check")

print("\n FIN")
