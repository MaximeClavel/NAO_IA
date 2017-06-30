# coding: utf-8
import random
import json
import requests

from Carte import*;

parite = 0
couleur = 0
regle = 0

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

# Verification si le mec est prophete quand il le demande
def isProphete():
    url = 'http://79.137.38.211/api/public/index.php/'
    url_jouerCoup = 'jouercoup'
    url_getHand = 'cards'

    reqGetHand = requests.get(url + url_getHand)

    if reqGetHand.status_code == 200:

        getHandJson = json.loads(reqGetHand.text)
        # print reqGetHand.text

        if getHandJson['turn'] == 0:
            print''
            print'Someone is PROPHETE'
            return


# Main
if __name__ == '__main__':

    # Init des variables de verif
    validiteCouleur = 1
    validiteParite = 1
    cartes = []             # Tableau de carte à récupérer
    carte = Carte(0, 0)     # Instance de carte

    url = 'http://79.137.38.211/api/public/index.php/'
    url_cardPlayed = 'cards'
    reqGetCard = requests.get(url + url_cardPlayed)

    # Init de la carte TEST > 10 de trefle
    # carte = Carte(0, 10)

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

    # Plusieurs regles ?
    nbregle = random.randint(1, 2)
    if nbregle == 1:
        regle = 1
    else:
        regle = 2

    # Nb Regle defini au hasard
    print ('')
    print ('Nombre de regle : ')
    print (regle)
    print ('')

    # Requete de recupreation de carte
    # Tant que perosnne n'est prophete set carte en verif
    while True:


        if reqGetCard.status_code == 200:

            getCardJson = json.loads(reqGetCard.text)

            if len(getCardJson['card_played']) != 0 and getCardJson['prophete'] == '1':
                print''
                print'Un joueur à jouer'
                cartes = getCardJson['card_played']
                print cartes

            for x in range (0,len(cartes)):
                # Regle 1
                if regle == 1:
                    if parite == 0 and iscardpair(x) == True:
                        print ('Carte paire; regle respectée')
                    elif parite == 1 and iscardpair(x) == False:
                        print ('carte impaire; regle respectée')
                    else:
                        print ('regle parité non resepectee ! ')
                        validiteParite = 0

                # Regle 2
                if regle == 2:
                    if parite == 0 and iscardpair(x) == True:
                        print ('Carte paire; regle respectée')
                    elif parite == 1 and iscardpair(x) == False:
                        print ('carte impaire; regle respectée')
                    else:
                        print ('regle parité non resepectee ! ')
                        validiteParite = 0

                    if couleur == 0 and iscardnoir(x) == True:
                        print ('carte noir; règle respectée')
                    elif couleur == 1 and iscardnoir(x) == False:
                        print ('carte rouge; règle respectée')
                    else:
                        print ('regle couleur non resepectee ! ')
                        validiteCouleur = 0

                if validiteCouleur == 1 and validiteParite == 1:
                    print ('')
                    print ('carte valide')
    # End request true pour prophete

    # Requete pour savoir si le mec à jouer une carte et Test de cette carte
    # TODO: etudier la valider de plusieurs cartes jouée

    if reqGetCard.status_code == 200:

        getCardJson = json.loads(reqGetCard.text)

        if len(getCardJson['card_played']) != '0' and getCardJson['prophete'] == '0':
            print''
            if len(getCardJson['card_played']) == 1:
                print'Un joueur à jouer une carte'
                carte = getCardJson['card_played'][0]
                print carte

        # Regle 1
        if regle == 1:
            if parite == 0 and iscardpair(carte) is True:
                print ('Carte paire; regle respectée')
            elif parite == 1 and iscardpair(carte) is False:
                print ('carte impaire; regle respectée')
            else:
                print ('regle parité non resepectee ! ')
                validiteParite = 0

        # Regle 2
        if regle == 2:
            if parite == 0 and iscardpair(carte) is True:
                print ('Carte paire; regle respectée')
            elif parite == 1 and iscardpair(carte) is False:
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
            # POST si LA carte est bonne !!
            print ('carte valide')
