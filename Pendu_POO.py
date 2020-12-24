

class MotJoueur1:
    # PARTIE  1 --------------------------------------------------------------------------------------------------------
    # creation d une classe pour la saisie du joueur 1 :
    def saisieJoueur1(self):
        motJoueur1=input("J1 : Veuillez saisir un mot")

        return motJoueur1

    # FONCTION : Test si le mot ne contient pas de chiffre :
    def afficherSaisieJoueur1(self,motMystere):

        while MotJoueur1.checkChiffre(self,motMystere) == True:
            print("JOUEUR 1 ! Merci de ressaisir votre mot")
            motMystere=MotJoueur1.saisieJoueur1(self)

        print("JOUEUR 1 : Votre mot est validé")
        return motMystere

    # FONCTION : Test si un chiffre est dans le mot :
    def checkChiffre(self, testmot):
        for cpt in range(0, len(testmot)):
            x = testmot[cpt].isdigit()
            if x == True:
                return True

    # FONCTION : cache le mot du joueur 1 en "*" :
    def cacheMot(self, motEtoile):

        motEtoile = list(motEtoile)

        index = 0
        while index <= len(motEtoile) - 1:
            motEtoile[index] = "*"
            index = index + 1

        print(motEtoile)
        # RETOURNE le mot du joueur 1 sans les *
        return motEtoile


class MotJoueur2:
    # PARTIE  2 --------------------------------------------------------------------------------------------------------
    # creation d une class pour la saisie du joueur 2 :

    pv = 5

    def ___init___(self,pv):

        self.pv = pv

    # FONCTION SAISIE JOUEUR 2
    def saisieJ2(self):

        lettre = input("JOUEUR 2  saisie une lettre")
        return lettre

    # FONCTION : test si presence d un chiffre dans la saisie du joueur 2 :
    def checkChiffreLettre(self, lettre):

        continuer = True

        while continuer == True:
            if lettre.isdigit() == True:
                print("C'est un CHIFFRE")
                lettre = input("JOUEUR 2 : Saisir une lettre")
                continuer = True

            elif lettre.isdigit() == False:
                continuer = False
                return lettre
    # FAIRE UNE FONCTION VIES AVEC ET SANS S
    def vie(self,pv):
        if pv <= 1:
            return "vie"
        else:
            return "vies"


    # FONCTION : SI une lettre est trouvé alors l étoile devient une lettre
    def scanLettreDansMot(self,lettre,mot,motEtoile):

        if lettre not in mot:

            self.pv= self.pv-1

            print("La lettre N'EST PAS présente. Il vous reste : ",self.pv)


        else:
            for i in range(0, len(mot)):

                    if lettre == mot[i]:
                        motEtoile[i] = lettre
                        print("La lettre est bien dans le mot", motEtoile)


    # FONCTION : retourne la saisie du joueur 2 :
    def saisieJoueur2(self):
        saisieJoueur2 = input("JOUEUR 2 : Veuillez saisir une lettre.")
        return saisieJoueur2

    # FONCTION : compare 2 mots en eux :
    def comparaison(self,a,b):

        return a == b

    # FOONCTION : transforme le mot en liste
    def transformationListe(self, mot):
        mot = list(mot)
        return mot


joueur1 = MotJoueur1()
motJ1 = joueur1.afficherSaisieJoueur1(joueur1.saisieJoueur1())
motEtoile = joueur1.cacheMot(motJ1)

# 5 est le nombre de vie du joueur 2
joueur2 = MotJoueur2()

# FONCTION : cree une liste de la saisie du joueur 1 pour que ma boucle marche
transformationMotJ1 = joueur2.transformationListe(motJ1)


while not joueur2.comparaison(transformationMotJ1, motEtoile) and joueur2.pv >0 :

    lettreJoueur2 = joueur2.checkChiffreLettre(joueur2.saisieJoueur2())

    joueur2.scanLettreDansMot(lettreJoueur2,motJ1,motEtoile)

print("Partie terminé, votre nombre de vie est de",joueur2.pv)

