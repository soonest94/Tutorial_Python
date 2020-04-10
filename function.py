def chat():
    print("A: Hola como estas?")
    print("B: Bien bien y tu?")

chat()

def chat(name1, name2):
    print("%s: Hola como estas?" % name1)
    print("%s: Estoy un poco cansado." % name2)
    print("%s: Que le pasa?" % name1)

chat("Pedro", "Martin")

def chat(name1, name2, cost):
    print("%s: Perdon, Que es esto?" % name1)
    print("%s: Esto un naranja." % name2)
    print("%s: Vale. Cuanto cuesta esto?" % name1)
    print("%s: Cuesta %d euros." % (name2, cost))

chat("Pedro", "Martin", 5)


def dsum(a, b):
    result = a + b
    return result

d = dsum(2, 4)
print(d)

def dsum2(a, b):
    result = a + b
    print(result)

d = dsum2(5, 4)
print(d)


###########################################

################Hola bot###################
#Say "Buenos dias" until 11.
#Say "Buenas tardes" until 18.
#Say "Buenas noches" until 24.

def hola(name, time):
    if time < 12:
        print("Buenos dias, " + name)
    elif time >=12 and time <=18:
        print("Buenas tardes, " + name)
    else:
        print("Buenas noches, " + name)

hola("Sr.Pedro", 10)
hola("Don quichotte", 14)
hola("Sra.Belle", 20)
