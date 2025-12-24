vrai = True
faux = False
print(type(vrai))
print(type(faux))
print(5==5)
print (5==3)
print (5<=5)
print (5<5)
print (5!=5)
print("5"==5)
print ("a"=="b")
print("a"=="A")
print("a"!="b")
print("a">"b")
print("a">"A")
print("a"<"b")
print("a"<"A")

print(True and True)
print(False and False)
print(False and False)

email = 'test@test.fr'
mdp = 'test' 
connection_reussi = email =="test@test.fr" and mdp== "test"
print(connection_reussi)
email = 'test@test.fr'
mdp = 'test1' 
connection_reussi = email =="test@test.fr" and mdp== "test"
print(connection_reussi)
print(True or True)
print (True or False)
print(False or False)

identifiant = "toto"
identifiant_valide = email== "test@test.fr" or identifiant == "toto"

print(not True)
print (not False)