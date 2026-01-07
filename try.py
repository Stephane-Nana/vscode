
try:
    x= 2
    print(x)
except NameError as e:
    print("message d'erreur : " + str(e))
except:
   print("erreur detecter")
else:
   print("aucune erreur a signaler")
finally:
    print("traitement terminer")
y=10
print(y)

x= -1
if x<0:
    raise Exception("nombre negatif interdit !")#ici je provoque une erreuret peut import le code que j'ecris en bas de cette erreur, il ne sera pas excecuter
z= 1
print(z)