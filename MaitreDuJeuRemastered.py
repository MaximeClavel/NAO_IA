# coding: utf-8
import random
import json
import requests

from Carte import *

# Definition de variables global
parite = 0
couleur = 0
regle = 0
inferieur = 0
superieur = 0
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

    setRegleInferieurOrAndSuperieur()
    print ('regle superieur a ', nbSuperieur)
    print ('regle inferieur a ', nbInferieur)


    # Plusieurs règles ?
    nbregle = random.randint(1, 4)

    if nbregle == 1:
        regle = 1
    elif nbregle == 2:
        regle = 2
    elif nbregle == 3:
        regle = 3
    elif nbregle == 4:
        regle = 4

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
    print ('')
    if not iscardpair(carteParite):
        print ('Carte impaire; regle respectee')
        validiteParite = 1
    else:
        print ('carte pair; regle non respectee')

def testCouleur(carteCouleyr):
    global validiteCouleur
    if not iscardnoir(carteCouleyr):
        print ('carte rouge; regle non respectee')
        validiteCouleur = 1
    else:
        print ('carte noir; regle respectee')

def testInferieurEtSuperieur(carteInferieur):
    global validiteInferieur
    global validiteSuperieur

    # Multi check
    if regle == 4:
        if carteInferieur.valeur > nbSuperieur and carteInferieur.valeur < nbInferieur:
            print ('carte de valeur inferieur; regle respecte')
            print ('carte de valeur superieur; regle respecte')
            validiteInferieur = 1
            validiteSuperieur = 1
        if carteInferieur.valeur < nbSuperieur and carteInferieur.valeur < nbInferieur:
            print ('carte de valeur superieur; regle respectee > val carte > ', carteInferieur.valeur)
        else:
            print ('Valeur devrait etre superieur')

        if carteInferieur.valeur > nbSuperieur and carteInferieur.valeur > nbInferieur:
            print ('carte de valeur inferieur; regle respectee > val carte > ', carteInferieur.valeur)
        else:
            print ('Valeur devrait etre inferieur')

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

#  Vérification de parité
def iscardpair(cartep):
    if cartep.parite == 0:
        return True
    else:
        return False

# Couleur
def iscardnoir(carteo):
    if carteo.couleur == 0:
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

                    print (carteTmp.valeur, carteTmp.symbole, ' > Carte tmp')

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

                    if validiteCouleur == 1 and validiteParite == 1 and validiteSuperieur == 1 and validiteSuperieur == 1:
                        print ('')
                        print ('carte valide')
                    else:
                        print ('')
                        boolProphete = False
                        break

                # Retour du POST pour prophete
                urlProphete = 'http://79.137.38.211/api/public/index.php/tristan'
                if boolProphete:
                    reqPostProphete = requests.post(url, True)
                    print ('True : La main du joueur fait qu il est prophete')
                elif boolProphete:
                    reqPostProphete = requests.post(url, False)
                    print ('False : La main du joueur fait qu il n est prophete')

            # If test Une carte SANS prophete
            else:
                print'Un joueur a joué une carte!!! '
                print('')

                # TODO: Get ALL CARDS FROM PLAYER WHO SAYS HE IS PROPHETE

                for x in getCardJson['cards']:

                    carteTmp = Carte(x[0], x[1])

                    print (carteTmp.valeur, carteTmp.symbole , ' > Carte tmp')

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

                    if validiteCouleur == 1 and validiteParite == 1 and validiteSuperieur == 1 and validiteSuperieur == 1:
                        print ('')
                        #TODO: POST si LA carte est bonne !! > ?
                        print (x,' : carte valide')
        break

# Main
if __name__ == '__main__':
    c = Carte(0, 10) #TODO: Load list cards from API
    generateregle()
    isCardPlayedValidAndMaybeProphete()