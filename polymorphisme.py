class vehicule:
    def __init__(self,marque,modele):
        self.marque = marque
        self.modele = modele
    def moove(self):
        print ("roule")
class voiture(vehicule):
    pass
class bateau(vehicule):
    def moove(self):
        print("navigue !")
class avion(vehicule):
    def moove(self):
        print("vole")
v1 = voiture("ford","mustang")
b1 = bateau("ibiza","20 touring")
a1 = avion("boing","747")

for carracteristique in (v1,b1,a1):
    print(carracteristique.marque, carracteristique.modele)
    carracteristique.moove()