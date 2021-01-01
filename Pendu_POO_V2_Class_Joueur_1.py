from Pendu_POO_V2_Class_Joueur import Joueur

class Joueur1(Joueur):
    def __init__(self,pseudo):
        super().__init__(pseudo)

    # creation d une classe pour la saisie du joueur 1 :

    #FONCTION saisie d'un MOT
    def saisieJoueur(self):
        print(super().getPseudo()," : Veuillez saisir un mot")

        motJoueur=input("Saisir mot ----> ")
        return motJoueur

    # FOONCTION : transforme le mot en liste
    def transformationListe(self, mot):
        mot = list(mot)
        return mot

    # FONCTION : Test si le mot contient un chiffre :
    def checkChiffre(self,motJoueur):
        for cpt in range(0, len(motJoueur)):
            x = motJoueur[cpt].isdigit()
            if x == True:
                while x == True:
                    motJoueur = input("Merci de ressaisir votre mot")
                    for cpt in range(0, len(motJoueur)):
                        x = motJoueur[cpt].isdigit()
                return motJoueur

        print("Votre mot est enregistré")
        return motJoueur

    # FONCTION : cache un mot sous forme "*" :
    def cacheMot(self, motEtoile):

        motEtoile = list(motEtoile)

        index = 0
        while index <= len(motEtoile) - 1:
            motEtoile[index] = "*"
            index = index + 1

        print(motEtoile)
        # RETOURNE le mot du joueur 1 sans les *
        return motEtoile
