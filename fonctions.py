def fonction():#une fonction en python commence toujours par le mot cle def
    print("bienvenue sur mon guide ptthon")
fonction()#ici nous appelons notre fonction

def essai(parametre):
    print ("le parametre est : "+parametre)
essai("ange")

def prenom_nom(prenom, nom):
    print("mon prenom est : "+prenom+ " et mon nom est : "+nom)
prenom_nom("yves", "rocher")

def essai1(m="valeur"):
    print(m)
essai1("other")
essai1()

def carre(x):
    return x**2
test = carre(5)#ici nnous avons appeler notre fonction carre dans notre variable test
print(test)

def factoriel(n):#nous allons voir le cas d'une fonction recursive
    if n == 0 or n== 1:
        return 1
    else:
        return n*factoriel(n-1)
print(factoriel(5))