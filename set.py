#un set est une structure de donnee qui permet de stocker des donnees qui ne sont ni ordonnees ni indexer
set_vide = set()
print(set_vide)
jus = {"pomme", "ananas", "orange"}
print(jus)
set_vide.add (2)
print(set_vide)
jus.remove("pomme")
print(jus)
#jus.remove("tomate")ici on aura une erreur vu que tomate n'existe pas
print (jus)
jus.discard("tomate")#ici nous n'aurons pas d'erreur
print(jus)