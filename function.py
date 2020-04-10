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
