dictionnaire_vide = {}
personne ={
    "nom" : "yves",
    "prenom" : "fred"
}
print(personne)
print(type(personne))
print(len(personne))
print(personne["nom"])
print(personne.keys)
print(personne.values)
print(personne.items)#ici le resultat sera afficher sous forme de tuple
personne ["prenom"] = "Nolan"
print(personne)
personne["age"] = 20
print (personne)
personne.pop("age")
print(personne)
personne2 = personne.copy()
print(personne)
print(personne2)