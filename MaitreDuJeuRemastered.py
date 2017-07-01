# coding: utf-8
import random
import json
import requests

from Carte import*;

# Definition de variables global
parite = 0
couleur = 0
regle = 0
boolProphete = True
url = 'http://79.137.38.211/api/public/index.php/'
url_cardPlayed = 'cards'
validiteCouleur = 1
validiteParite = 1
cartes = []             # Tableau de carte à récupérer
carte = Carte(0, 0)     # Instance de carte

# Définition de la règle ET determination du nombre de règles à appliquer
def generateregle():
    global parite
    global couleur
    global regle

    parite = random.randint(0,1)
    couleur = random.randint(0,1)

    if parite == 0:
        print ('règle paire')
    else:
        print ('règle impaire')

    if couleur == 0:
        print ('règle noir')
    else:
        print ('règle rouge')

    # Plusieurs règles ?
    nbregle = random.randint(1, 2)
    if nbregle == 1:
        regle = 1
    else:
        regle = 2

    # Nb Règles definies au hasard
    print ('')
    print ('Nombre de regle : ')
    print (regle)
    print ('')

# Maitre du jeu
def idcardvalide(Carte):
    print ('')
    if parite == 0 and iscardpair(Carte) == True:
        print ('Carte paire; règle respectée')
    elif parite == 1 and iscardpair(Carte) == False:
        print ('carte impaire; règle non respectée')

    if couleur == 0 and iscardnoir(Carte) == True:
        print ('carte noir; règle respectée')
    elif couleur == 1 and iscardnoir(Carte) == False :
        print ('carte rouge; règle non respectée')

#  Vérification de parité
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

# Verification de la validite d'une seul carte TEST sans connexion à l'API

def isCardPlayedValidTEST(carte):
    global url
    global url_cardPlayed
    global validiteCouleur
    global validiteParite

    if regle == 1:
        if parite == 0 and iscardpair(carte) is True:
            print ('Carte paire; regle respectée')
        elif parite == 1 and iscardpair(carte) is False:
            print ('carte impaire; regle respectée')
        else:
            print ('regle parité non resepectee ! ')
            validiteParite = 0

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
        # TODO: POST si LA carte est bonne !!
        print ('carte valide')


# Verification de la validite d'une seul carte
def isCardPlayedValid():
    global url
    global url_cardPlayed
    global validiteCouleur
    global validiteParite

    # Début du ping en folie
    while True:
        reqGetCard = requests.get(url + url_cardPlayed) #TODO: Verif URL
        if reqGetCard.status_code == 200:

            getCardJson = json.loads(reqGetCard.text)

            if len(getCardJson['card_played']) != '0' and getCardJson['prophete'] == '0':
                print''
                if len(getCardJson['card_played']) == 1:
                    print'Un joueur à jouer une carte'
                    carte = getCardJson['card_played'][0]
                    print carte
            for x in range(0, len(cartes)):
                # Regle 1
                if regle == 1:
                    if parite == 0 and iscardpair(x) is True:
                        print ('Carte paire; regle respectée')
                    elif parite == 1 and iscardpair(x) is False:
                        print ('carte impaire; regle respectée')
                    else:
                        print ('regle parité non resepectee ! ')
                        validiteParite = 0

                # Regle 2
                if regle == 2:
                    if parite == 0 and iscardpair(x) is True:
                        print ('Carte paire; regle respectée')
                    elif parite == 1 and iscardpair(x) is False:
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
                    #TODO: POST si LA carte est bonne !! > ?
                    print (x,' : carte valide')

        break


# Verification si le mec est prophete quand il le demande
def isProphete():
    # Requete de recupreation de carte
    # Tant que perosnne n'est prophete set carte en verif
    global url
    global url_cardPlayed
    global validiteCouleur
    global validiteParite

    while True:  # Début du ping en folie
        reqGetCard = requests.get(url + url_cardPlayed)
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
                else:
                    print ('')
                    boolProphete = False
                    break
        break

    if len(getCardJson['card_played']) != 0 and getCardJson['prophete'] == '1' and boolProphete == True:
        print ('True : La main du joueur fait qu il est prophete')
        # TODO Requete de prophete TRUE
    elif len(getCardJson['card_played']) != 0 and getCardJson['prophete'] == '1' and boolProphete == False:
        print ('False : La main du joueur fait qu il n est prophete')
        # TODO Requete de prophete False

# Main
if __name__ == '__main__':
    c = Carte(0, 10) #TODO: Load list cards from API
    generateregle()
    isCardPlayedValidTEST(c)