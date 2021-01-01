class Joueur:

    pseudo = None
    def __init__(self,pseudo):
        self.pseudo = pseudo

    #FONCTION : permet de changer le pseudo
    def pseudoJoueur(self):
        pseudo = input("Veuillez saisir un pseudo de joueur")
        self.pseudo = pseudo
        print("Votre pseudo est --- ",self.pseudo," --- maintenant")

    #FONCTION retourne le pseudo de l objet
    def getPseudo(self):
        return self.pseudo







