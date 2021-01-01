from Pendu_POO_V2_Class_Joueur_1 import Joueur1
from Pendu_POO_V2_Class_Joueur_2 import Joueur2

# CREATION des objets joueurs

joueur1 = Joueur1("")
pseudo = joueur1.pseudoJoueur()

print("---------------------------------------------------------------------------------------------")

joueur2 = Joueur2("",5)
joueur2.pseudoJoueur()

print("---------------------------------------------------------------------------------------------")

# Phrase qui confirme bien que les speudo on été changé
print("Joueur 1 devient", joueur1.getPseudo(), "\nJoueur 2 devient", joueur2.getPseudo())

print("---------------------------------------------------------------------------------------------")

# Stock la saisie du joueur 1 dans la variable pour plus tard faire une comparaison
motJoueur1=joueur1.saisieJoueur()

# Scan le mot à la recherche d'une lettre dans la saisie
motJoueur1 = joueur1.checkChiffre(motJoueur1)

print(motJoueur1)
# Transforme le mot du joueur 1 en étoile
motEtoile=joueur1.cacheMot(motJoueur1)

print("---------------------------------------------------------------------------------------------")

# FONCTION : cree une liste de la saisie du joueur 1
transformationMotJ1 = joueur1.transformationListe(motJoueur1)


while not joueur2.comparaison(transformationMotJ1, motEtoile) and joueur2.pv >0 :
    lettreJoueur2 = joueur2.saisieJoueur2()

    joueur2.scanLettreDansMot(lettreJoueur2,motJoueur1,motEtoile)

print("Partie terminée, votre nombre de vie est de",joueur2.pv)
