# coding: utf-8
import random

from Carte import*;

parite = 0
couleur = 0

carte = Carte

# Définition de la règle
def generateregle():
    parite = random.randint(0,1)
    couleur = random.randint(0,1)
    if parite == 0:
        print ('regle paire')
    else:
        print ('regle impaire')

    if couleur == 0:
        print ('regle noir')
    else:
        print ('regle rouge')

# Maitre du jeu
def idcardvalide(Carte):
    print ('')
    if parite == 0 and iscardpair(Carte) == True:
        print ('Carte paire; regle respectée')
    elif parite == 1 and iscardpair(Carte) == False:
        print ('carte impaire; regle non respectée')

    if couleur == 0 and iscardnoir(Carte) == True:
        print ('carte noir; règle respectée')
    elif couleur == 1 and iscardnoir(Carte) == False :
        print ('carte rouge; règle non respectée')

# Parité
def iscardpair(Carte):
    if Carte.parite == 0:
        return True
    else:
        return False

# Couleur
def iscardnoir(Carte):
    if Carte.couleur == 0:
        return True
    else:
        return False

# Main
if __name__ == '__main__':

    # Init des variables de verif
    validiteCouleur = 1;
    validiteParite = 1;

    # Init de la carte TEST
    carte = Carte(0, 10)

    # Gen de la regle
    parite = random.randint(0, 1)
    couleur = random.randint(0, 1)
    if parite == 0:
        print ('regle paire')
    else:
        print ('regle impaire')

    if couleur == 0:
        print ('regle noir')
    else:
        print ('regle rouge')

    # Carte de la validité de la carte
    print ('')
    if parite == 0 and iscardpair(carte) == True:
        print ('Carte paire; regle respectée')
    elif parite == 1 and iscardpair(carte) == False:
        print ('carte impaire; regle respectée')
    else:
        print ('regle parité non resepectee ! ')
        validiteParite = 0

    if couleur == 0 and iscardnoir(carte) == True:
        print ('carte noir; règle respectée')
    elif couleur == 1 and iscardnoir(carte) == False:
        print ('carte rouge; règle respectée')
    else:
        print ('regle couleur non resepectee ! ')
        validiteCouleur = 0

    if validiteCouleur == 1 and validiteParite == 1:
        print ('')
        print ('carte valide')