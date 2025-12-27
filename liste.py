Liste = []
jus = ["ananas", "orange", "pommes"]
nombre = [1, 2, 12, 20, 3]
liste_mixte = ["mixte", 1, 2.5]
print(type(jus))
print(type(liste_mixte))
print(len(jus))
print(nombre[0])
print(nombre[-5])
print (jus[1:3])

jus[2]= "citron"
print(jus)
jus[1:2]= "lemon", "pamplemouse", "fraise"
print(jus)
print (len(jus))
jus.append("raisin")
print(jus)
jus.insert(1,'kiwi')
print(jus)
jus.extend(["peche", "poire"])
print(jus)
jus.remove("poire")
print(jus)
jus.pop(1)
print(jus)
jus.reverse()
print(jus)
jus.sort()
print(jus)
jus2 = jus
print(jus2)
jus[1] = "clone"
print(jus)
print(jus2)
jus3 = jus.copy()
print(jus3)
jus[1] = "mangue"
print(jus)
print(jus2)
print(jus3)
new_liste = jus + nombre + liste_mixte
print(new_liste)
matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
element = matrice[1][2]
print(element)