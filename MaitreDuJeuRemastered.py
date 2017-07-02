# coding: utf-8
import random
import json

import requests
from ast import literal_eval

from Carte import *

# Definition de variables global
parite = 0
couleur = 0
regle = 0
inferieur = 0
superieur = 0
validiteEgalite = 0
nbEgalite = 0
nbSuperieur = 0
nbInferieur = 0
validiteCouleur = 0
validiteParite = 0
validiteInferieur = 0
validiteSuperieur = 0
# End definition regle

boolProphete = True
url = 'http://79.137.38.211/api/public/index.php/'
url_cardPlayed = 'cards'
cartes = []             # Tableau de carte à récupérer
carte = Carte(0, 0)     # Instance de carte

# Définition de la règle ET determination du nombre de règles à appliquer
def generateregle():
    global parite
    global couleur
    global regle
    global inferieur
    global superieur
    global nbInferieur
    global nbSuperieur
    global nbEgalite

    parite = random.randint(0,1)
    couleur = random.randint(0,1)

    #Set regle card egalité random
    #nbEgalite = random.randint(1,13)

    if parite == 0:
        print ('règle paire')
    else:
        print ('règle impaire')

    if couleur == 0:
        print ('règle noir')
    else:
        print ('règle rouge')

    setRegleInferieurOrAndSuperieur()
    print ('regle inferieur a ', nbInferieur)
    print ('regle superieur a ', nbSuperieur)

    if nbEgalite != 0:
        print ('la valeur de la carte doit etre de = ', nbEgalite)

    # Plusieurs règles ?
    #nbregle = random.randint(1, 4)
    nbregle = 2
    if nbregle == 1:
        regle = 1
    elif nbregle == 2:
        regle = 2
    elif nbregle == 3:
        regle = 3
    elif nbregle == 4:
        regle = 4
    elif nbregle == 5:
        regle = 5

    # Nb Règles definies au hasard
    print ('')
    print 'Nombre de regle : ', regle
    print ('')

# Instance des nombres inferieur et superieur
def setRegleInferieurOrAndSuperieur():
    global nbInferieur
    global nbSuperieur
    nbSuperieur = random.randint(1, 13)
    nbInferieur = random.randint(1, 13)

def testParite(carteParite):
    global validiteParite
    global parite
    print ('')
    if iscardpair(carteParite) and parite == 0:
        print ('Carte pair; regle respectee')
        validiteParite = 1
    elif iscardpair(carteParite) and parite == 1:
        print ('Carte pair; regle non respectee')

    if not iscardpair(carteParite) and parite == 1:
        print ('carte impair; regle respectee')
        validiteParite = 1
    elif not iscardpair(carteParite) and parite == 0:
        print ('carte impair; regle non respectee')

def testCouleur(carteCouleur):
    global validiteCouleur
    global couleur
    if iscardnoir(carteCouleur) and couleur == 0:
        print ('carte noir; regle respectee')
        validiteCouleur = 1
    elif iscardnoir(carteCouleur) and couleur == 1:
        print ('carte noir; regle non respectee')

    if not iscardnoir(carteCouleur) and couleur == 1:
        validiteCouleur = 1
        print ('carte rouge; regle respectee')
    elif not iscardnoir(carteCouleur) and couleur == 0:
        print ('carte rouge; regle non respectee')

def testInferieurEtSuperieur(carteInferieur):
    global validiteInferieur
    global validiteSuperieur

    # Multi check
    if regle == 4:
        valueDeLaCarte = int(carteInferieur.valeur)

        if valueDeLaCarte > nbSuperieur and valueDeLaCarte < nbInferieur:
            print ('carte de valeur inferieur; regle respecte')
            print ('carte de valeur superieur; regle respecte')
            validiteInferieur = 1
            validiteSuperieur = 1
        else:
            if valueDeLaCarte < nbSuperieur:
                print ('NO : Valeur devrait etre inferieur pour la regle superiorite')
            if valueDeLaCarte > nbSuperieur:
                print ('YES : Regle superieur respectee')
                validiteSuperieur = 1

            if valueDeLaCarte > nbInferieur:
                print ('NO : Valeur devrait etre superieur pour la regle inferiorite')
            if valueDeLaCarte < nbInferieur:
                print ('YES : Regle inferieur respectee')
                validiteInferieur = 1

    # Random entre Superieur et Inferieur
    intRandom = random.randint(0,1)
    if regle == 3 and intRandom == 1:
        if carteInferieur.valeur > nbSuperieur:
            print ('carte de valeur superieur; regle respectee > val carte > ', carteInferieur.valeur)
            validiteSuperieur = 1
        else:
            print ('carte de valeur superieur; regle non respectee > val carte > ', carteInferieur.valeur)

    if regle == 3 and intRandom == 0:
        if  carteInferieur.valeur < nbSuperieur:
            validiteInferieur = 1
            print ('carte de valeur inferieur; regle respectee > val carte > ', carteInferieur.valeur)
        else:
            print ('carte de valeur inferieur; regle non respectee > val carte > ', carteInferieur.valeur)


def testEgaliteCard(carteEgalite):
    global validiteEgalite
    global nbEgalite

    if nbEgalite == carteEgalite.valeur:
        print ('la val carte est bien egale à la valeur random de la regle')
        validiteEgalite = 1
    else:
        print ('la val carte n est pas egale la valeur random de la regle')

#  Vérification de parité
def iscardpair(cartePairImpair):
    if cartePairImpair.parite == 0:
        return True
    else:
        return False

# Couleur
def iscardnoir(carteNioirTest):
    if carteNioirTest.couleur == 0 or  carteNioirTest.couleur == 3:
        return True
    else:
        return False

# Verification de la validite d'une seul carte TEST sans connexion à l'API

def isCardPlayedValidTEST(carteDeTest):
    global url
    global url_cardPlayed
    global validiteCouleur
    global validiteParite

    if regle == 1:
        if parite == 0 and iscardpair(carteDeTest) is True:
            print ('Carte paire; regle respectée')
        elif parite == 1 and iscardpair(carteDeTest) is False:
            print ('carte impaire; regle respectée')
        else:
            print ('regle parité non resepectee ! ')
            validiteParite = 0

    if regle == 2:
        if parite == 0 and iscardpair(carteDeTest) is True:
            print ('Carte paire; regle respectée')
        elif parite == 1 and iscardpair(carteDeTest) is False:
            print ('carte impaire; regle respectée')
        else:
            print ('regle parité non resepectee ! ')
            validiteParite = 0

        if couleur == 0 and iscardnoir(carteDeTest) == True:
            print ('carte noir; règle respectée')
        elif couleur == 1 and iscardnoir(carteDeTest) == False:
            print ('carte rouge; règle respectée')
        else:
            print ('regle couleur non resepectee ! ')
            validiteCouleur = 0

    if validiteCouleur == 1 and validiteParite == 1 and validiteSuperieur == 1 and validiteSuperieur == 1:
        print ('')
        # TODO: POST si LA carte est bonne !!
        print ('carte valide')


# Verification de la validite d'une seul carte
def isCardPlayedValidAndMaybeProphete():
    global url
    global url_cardPlayed
    global validiteCouleur
    global validiteParite
    global carte
    global boolProphete

    # Début du ping en folie
    while True:
        reqGetCard = requests.get(url + url_cardPlayed) #TODO: Verif URL

        if reqGetCard.status_code == 200:

            getCardJson = json.loads(reqGetCard.text)

            # If null
            if not getCardJson:
                return

            # If joueur dit PROOOPPHHETEE
            elif getCardJson and getCardJson['turn'] == '0':
                print ('Le joueur DIT PROOOPPHHETTEE')
                for x in getCardJson['cards']:

                    carteTmp = Carte(x[0], x[1])

                    print (carteTmp.symbole, carteTmp.valeur, ' > Carte tmp')

                    print ('')

                    if regle == 1:
                       testParite(carteTmp)

                    if regle == 2:
                        testParite(carteTmp)
                        testCouleur(carteTmp)

                    if regle == 3:
                        testParite(carteTmp)
                        testCouleur(carteTmp)
                        testInferieurEtSuperieur(carteTmp)

                    if regle == 4:
                        testParite(carteTmp)
                        testCouleur(carteTmp)
                        testInferieurEtSuperieur(carteTmp)

                    if regle == 5:
                        testParite(carteTmp)
                        testCouleur(carteTmp)
                        testInferieurEtSuperieur(carteTmp)
                        testEgaliteCard(carteTmp)

                    if validiteCouleur == 1 and validiteParite == 1 and validiteSuperieur == 1 and validiteSuperieur == 1 and validiteEgalite == 1:
                        print ('')
                        print ('carte valide')
                    else:
                        print ('')
                        boolProphete = False
                        break

                # Retour du POST pour prophete
                urlProphete = 'http://79.137.38.211/api/public/index.php/tristan'
                if boolProphete:
                    requests.post(urlProphete, True)
                    print ('True : La main du joueur fait qu il est tristan')

                elif boolProphete:
                    requests.post(urlProphete, False)
                    print ('False : La main du joueur fait qu il n est tristan')

            # If test Une carte SANS prophete
            else:
                print'Un joueur a joué une carte!!! '
                print('')

                for x in getCardJson['cards']:

                    carteTmp = Carte(x[0], x[1])

                    print (carteTmp.symbole, carteTmp.valeur , ' > Carte tmp')

                    print ('')

                    if regle == 1:
                        testParite(carteTmp)

                    if regle == 2:
                        testParite(carteTmp)
                        testCouleur(carteTmp)

                    if regle == 3:
                        testParite(carteTmp)
                        testCouleur(carteTmp)
                        testInferieurEtSuperieur(carteTmp)

                    if regle == 4:
                        testParite(carteTmp)
                        testCouleur(carteTmp)
                        testInferieurEtSuperieur(carteTmp)

                    if regle == 5:
                        testParite(carteTmp)
                        testCouleur(carteTmp)
                        testInferieurEtSuperieur(carteTmp)
                        testEgaliteCard(carteTmp)

                    # Set du return
                    urlValiditeCard = 'http://79.137.38.211/api/public/index.php/card_valid'

                    if regle == 1:
                        if validiteCouleur == 1:
                            print ('')
                            requests.post(urlValiditeCard, True)
                            print (x,' : carte valide')
                    if regle == 2:
                        if validiteCouleur == 1 and validiteParite == 1:
                           # requests.post(urlValiditeCard, True)
                            print (x, ' : carte valide')
                    if regle == 3:
                        if validiteCouleur == 1 and validiteParite == 1 and validiteSuperieur == 1:
                            print ('')
                            requests.post(urlValiditeCard, True)
                            print (x, ' : carte valide')
                    if regle == 4:
                        if validiteCouleur == 1 and validiteParite == 1 and validiteSuperieur == 1 and validiteSuperieur == 1:
                            print ('')
                            requests.post(urlValiditeCard, True)
                            print (x, ' : carte valide')
        break

# Main
if __name__ == '__main__':
    #c = Carte(0, 10) #TODO: Load list cards from API
    generateregle()

    #Spam Api to play
    urlToSpamToPlay = 'http://79.137.38.211/api/public/index.php/cards'
    while True:
        reqGetSpamTurn = requests.get(urlToSpamToPlay)
        if reqGetSpamTurn.status_code == 200:
            if reqGetSpamTurn['nouveau_coup'] == '1':
                isCardPlayedValidAndMaybeProphete()