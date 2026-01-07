class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        print(f"bonjour, je m'appelle {self.prenom} {self.nom}")
class Etudiant(Utilisateur) :
    def __init__(self, nom, prenom, num_etudiant):
        super().__init__(nom, prenom)
        self.num_etudiant = num_etudiant
e1 = Etudiant("steph", "steven", 1234)
print(e1.nom, e1.prenom, e1.num_etudiant)
e1.se_presenter()