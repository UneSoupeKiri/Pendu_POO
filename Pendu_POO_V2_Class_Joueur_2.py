from Pendu_POO_V2_Class_Joueur import Joueur

class Joueur2(Joueur):
    def __init__(self,pseudo,pv):
        self.pv = pv
        super().__init__(pseudo)

    #FONCTION saisie d'une LETTRE !
    def saisieJoueur2(self):
        print(super().getPseudo()," : Veuillez saisir une lettre")

        motJoueur2=input("Saisir mot ----> ")
        return motJoueur2


    def afficheDessinPendu(self,pv):
        tab = [
            """                
               +-------+
               |       
               |       
               |
               |
               |
            ==============
                5 Vies:
            """
            ,
            """
               +-------+
               |       |
               |       
               |
               |
               |
            ==============
                4 Vies:
            """
            ,
            """
               +-------+
               |       |
               |       O
               |
               |
               |
            ==============
                3 Vies:
            """
            ,
            """
               +-------+
               |       |
               |       O
               |       |
               |
               |
            ==============
                2 Vies:
            """,
            """
               +-------+
               |       |
               |       O
               |      -|-
               |
               |
            ==============
                1 Vie:
            """,
            """          
               +-------+
               |       |
               |       O
               |      -|-
               |      | |
               |
            ==============
                0 Vies:
            """
        ]
        if pv == 5:
            print(tab[0])
        if pv == 4:
            print(tab[1])
        if pv == 3:
            print(tab[2])
        if pv == 2:
            print(tab[3])
        if pv == 1:
            print(tab[4])
        if pv == 0:
            print(tab[5])


    # FONCTION : vie et vieS
    def vie(self,pv):
        if pv <= 1:
            return "vie"
        else:
            return "vies"

    # FONCTION : SI une lettre est trouvé alors l étoile devient une lettre

    def scanLettreDansMot(self, lettre, mot, motEtoile):

        if lettre not in mot:

            self.pv = self.pv - 1

            print("La lettre N'EST PAS présente. Il vous reste : ", self.pv,self.vie(self.pv,))

            self.afficheDessinPendu(self.pv)

        else:
            for i in range(0, len(mot)):

                if lettre == mot[i]:
                    motEtoile[i] = lettre
                    print("La lettre est bien dans le mot", motEtoile)

    # FONCTION : compare 2 mots en eux :
    def comparaison(self,a,b):

        return a == b