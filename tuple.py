#un tuple est une structure de donner en programmation qui permet de stocker et organiser les donnees"
fruit = ("poire",) #tuple avec un seul element
fruits = ("pomme", "citron", "tomate", "fraise")
panier = fruits + fruit
print(type(fruit))
print(len(fruit))
print(len(fruits))
print(panier)
#on ne peut ni modifier ou supprimer les elements d'un tuple