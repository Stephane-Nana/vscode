x = 10
if x>5:
    print("x est plus grand que 5")
elif x>2:
    print("x est plutot plus grand que 2")
else :
    print("x est plus petit que 2")
fruit = ["pomme", "ananas", 'orange']
if "orange" in fruit:
    print("le fruit est present")
for f in fruit:
    print(f)
matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for ligne in matrice:
    print(ligne)
for ligne in matrice:
    for element in ligne:
        print(element)

set ={"python", "java", 'c++'}
for e in set:
    print(e)

personne = {
    "nom" : "yve",
    "prenom" : "fred"
}
for k in personne :
    print(personne[k])

for x in range (5):
    print("repetition")
for x in range (5):
    print(x)

for x in range(5, 10):
    print(x)

for x in range (5, 10, 2):#ici 2 represente le pas
    print (x)
for i in range (len(fruit)):
    print(fruit[i])
for i in range (-1, -len(fruit)-1, -1):
    print (fruit[i])

for i in range(5):
    if i==3:
        continue
    print(i)

for f in fruit:
    if f == "pomme":
        break
    print(f)
for f in fruit:
    if f == "lemon":
        break
    print (f)