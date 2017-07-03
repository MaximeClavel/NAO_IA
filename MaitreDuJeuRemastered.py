# coding: utf-8
import random
import json

import requests
from ast import literal_eval

from Carte import *

# Definition de variables global
parite = 0
couleur = 0
nombreRegles = 0
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
listReturned = []
listRegleActive = []
dictValueReglesActive = {}
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
    global nombreRegles
    global inferieur
    global superieur
    global nbInferieur
    global nbSuperieur
    global nbEgalite
    global listRsegleActive
    global dictValueReglesActive

    # Plusieurs règles ?
    randomEgaliteOuPair = random.randint(0,1)

    nbregle = random.randint(1, 3)

    if nbregle == 1:
        nombreRegles = 1
    elif nbregle == 2:
        nombreRegles = 2
    elif nbregle == 3:
        nombreRegles = 3

    # Nb Règles definies au hasard
    print ('')
    print ('Nombre de regle : ', nombreRegles)
    print ('')

    # Set regle card egalité random

    nbEgalite = random.randint(1, 13)

    print ('EGALITE : la valeur de la carte doit etre de = ', nbEgalite)
    dictValueReglesActive = {'egalite':nbEgalite}

    parite = random.randint(0, 1)
    couleur = random.randint(0, 1)
    if parite == 0:
        print ('PARITE : paire')
        dictValueReglesActive['parite'] = 'paire'
    else:
        print ('PARITE : impaire')
        dictValueReglesActive['parite'] = 'impaire'

    if couleur == 0:
        print ('COULEUR : noir')
        dictValueReglesActive['couleur'] = 'noir'
    else:
        print ('COULEUR : rouge')
        dictValueReglesActive['couleur'] = 'rouge'

    setRegleInferieurOrAndSuperieur()
    print ('INFERIEUR a ', nbInferieur)
    print ('SUPERIEUR a ', nbSuperieur)
    dictValueReglesActive['inferieur'] = nbInferieur
    dictValueReglesActive['superieur'] = nbSuperieur
    print ('')
    if nombreRegles == 1:
        intRandom1 = random.randint(0, 3)
        if intRandom1 == 0:
            listRegleActive.append('parite')
            print ('REGLE SELECT : PARITE')
        elif intRandom1 == 1:
            listRegleActive.append('couleur')
            print ('REGLE SELECT : COULEUR')
        elif intRandom1 == 2:
            listRegleActive.append('egalite')
            print ('REGLE SELECT : EGALITE')
        elif intRandom1 == 3:
            listRegleActive.append('infsup')
            print ('REGLE SELECT :  INFERIEUR SUPERIEUR')

    if nombreRegles == 2:
        intRandom2 = random.randint(0, 2)
        if intRandom2 == 0:
            listRegleActive.append('parite')
            listRegleActive.append('couleur')
            print ('REGLE SELECT : PARITE')
            print ('REGLE SELECT : COULEUR')
        if intRandom2 == 1:
            listRegleActive.append('parite')
            listRegleActive.append('infsup')
            print ('REGLE SELECT : PARITE')
            print ('REGLE SELECT :  INFERIEUR SUPERIEUR')
        if intRandom2 == 2:
            listRegleActive.append('couleur')
            listRegleActive.append('infsup')
            print ('REGLE SELECT : COULEUR')
            print ('REGLE SELECT :  INFERIEUR SUPERIEUR')

    if nombreRegles == 3:
        listRegleActive.append('parite')
        listRegleActive.append('couleur')
        listRegleActive.append('infsup')
        print ('REGLE SELECT : PARITE')
        print ('REGLE SELECT : COULEUR')
        print ('REGLE SELECT : INFERIEUR SUPERIEUR')


# Instance des nombres inferieur et superieur
def setRegleInferieurOrAndSuperieur():
    global nbInferieur
    global nbSuperieur
    nbSuperieur = random.randint(1, 12)
    nbInferieur = random.randint(nbSuperieur, 13)


def testParite(carteParite):
    global validiteParite
    global parite
    print ('')
    if iscardpair(carteParite) and parite == 0:
        print ('Carte pair; regle respectee')
        validiteParite = 1
    elif iscardpair(carteParite) and parite == 1:
        print ('Carte pair; regle non respectee')
        validiteParite = 0

    if not iscardpair(carteParite) and parite == 1:
        print ('carte impair; regle respectee')
        validiteParite = 1
    elif not iscardpair(carteParite) and parite == 0:
        print ('carte impair; regle non respectee')
        validiteParite = 0

def testCouleur(carteCouleur):
    global validiteCouleur
    global couleur
    if iscardnoir(carteCouleur) and couleur == 0:
        print ('carte noir; regle respectee')
        validiteCouleur = 1
    elif iscardnoir(carteCouleur) and couleur == 1:
        print ('COULEUR : regle non respectee')
        validiteCouleur = 0

    if not iscardnoir(carteCouleur) and couleur == 1:
        print ('carte rouge; regle respectee')
        validiteCouleur = 1
    elif not (iscardnoir(carteCouleur)) and couleur == 0:
        validiteCouleur = 0
        print ('COULEUR; regle non respectee')

def testInferieurEtSuperieur(carteInferieur):
    global validiteInferieur
    global validiteSuperieur

    # Multi check
    valueDeLaCarte = int(carteInferieur.valeur)

    if valueDeLaCarte >= nbSuperieur and valueDeLaCarte <= nbInferieur:
        print ('carte de valeur inferieur; regle respecte')
        print ('carte de valeur superieur; regle respecte')
        validiteInferieur = 1
        validiteSuperieur = 1
    else:
        if valueDeLaCarte <= nbSuperieur:
            print ('NO : Valeur devrait etre inferieur pour la regle superiorite')
            validiteSuperieur = 0
        if valueDeLaCarte >= nbSuperieur:
            print ('YES : Regle superieur respectee')
            validiteSuperieur = 1

        if valueDeLaCarte >= nbInferieur:
            print ('NO : Valeur devrait etre superieur pour la regle inferiorite')
            validiteInferieur = 0
        if valueDeLaCarte <= nbInferieur:
            print ('YES : Regle inferieur respectee')
            validiteInferieur = 1

    # Random entre Superieur et Inferieur
   # intRandom = random.randint(0,1)
  #  if nombreRegles == 3 and intRandom == 1:
  #      if carteInferieur.valeur >= nbSuperieur:
   #         print ('carte de valeur superieur; regle respectee > val carte > ', carteInferieur.valeur)
  #          validiteSuperieur = 1
  #      else:
  #          print ('carte de valeur superieur; regle non respectee > val carte > ', carteInferieur.valeur)

  #  if nombreRegles == 3 and intRandom == 0:
  #      if  carteInferieur.valeur <= nbSuperieur:
  #          validiteInferieur = 1
  #          print ('carte de valeur inferieur; regle respectee > val carte > ', carteInferieur.valeur)
  #      else:
 #           print ('carte de valeur inferieur; regle non respectee > val carte > ', carteInferieur.valeur)


def testEgaliteCard(carteEgalite):
    global validiteEgalite
    global nbEgalite

    value = int(carteEgalite.valeur)

    if nbEgalite == value:
        print ('EGALITE : OK la val carte est bien egale à la valeur random de la regle')
        validiteEgalite = 1
    else:
        print ('EGALITE : NON la val carte n est pas egale la valeur random de la regle')

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

    if nombreRegles == 1:
        if parite == 0 and iscardpair(carteDeTest) is True:
            print ('Carte paire; regle respectée')
        elif parite == 1 and iscardpair(carteDeTest) is False:
            print ('carte impaire; regle respectée')
        else:
            print ('regle parité non resepectee ! ')
            validiteParite = 0

    if nombreRegles == 2:
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

def selectRandomRgle(nbRegle, carteInst):
    global listReturned
    listRegle = ['parite', 'couleur', 'egalite', 'supinf']
    for i in range(1, nbRegle):
        randomNb = random.randint(1, len(listRegle))
        while listRegle[randomNb-1] in listReturned:
            randomNb = random.randint(1, len(listRegle))
        listReturned.append(listRegle[randomNb - 1])
    setRandomRegle(carteInst)

def setRandomRegle(carteRdm):
    global listRegleActive
    for x in listRegleActive:
        if x == 'parite':
            testParite(carteRdm)
        elif x == 'couleur':
            testCouleur(carteRdm)
        elif x == 'egalite':
            testEgaliteCard(carteRdm)
        elif x == 'infsup':
            testInferieurEtSuperieur(carteRdm)


# Verification de la validite d'une seul carte
def isCardPlayedValidAndMaybeProphete():
    global url
    global url_cardPlayed
    global validiteCouleur
    global validiteParite
    global carte
    global boolProphete
    global dictValueReglesActive
    global listRegleActive

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

                    print (carteTmp.symbole, carteTmp.valeur, ' : Carte tmp')

                    print ('')

                    if nombreRegles == 1:
                       testParite(carteTmp)

                    if nombreRegles == 2:
                        testParite(carteTmp)
                        testCouleur(carteTmp)

                    if nombreRegles == 3:
                        testParite(carteTmp)
                        testCouleur(carteTmp)
                        testEgaliteCard(carteTmp)

                    # Test des cartes dans la boucle FOR
                    if nombreRegles == 1:
                        if validiteCouleur == 1:
                            print ('')
                            print (x, ' : carte valide 1 regle')
                            boolProphete = False
                            print ('UNLUCKY')
                            break
                    if nombreRegles == 2:
                        if validiteCouleur == 1 and validiteParite == 1:
                            print ('')
                            print (x, ' : carte valide 2 regle')
                            boolProphete = False
                            print ('UNLUCKY')
                            break
                    if nombreRegles == 3:
                        if validiteCouleur == 1 and validiteParite == 1 and validiteSuperieur == 1:
                            print ('')
                            print (x, ' : carte valide 3 regles')
                            boolProphete = False
                            print ('UNLUCKY')
                            break

                    if nombreRegles == 4:
                        if validiteCouleur == 1 and validiteParite == 1 and validiteSuperieur == 1 and validiteSuperieur == 1:
                            print ('')
                            print (x, ' : carte valide 4 regles')
                            boolProphete = False
                            print ('UNLUCKY')
                            break

                # Retour du POST pour prophete
                urlProphete = 'http://79.137.38.211/api/public/index.php/tristan'
                if boolProphete:
                    requests.post(urlProphete, True)
                    print ('True : La main du joueur fait qu il est tristan')

                elif not boolProphete:
                    requests.post(urlProphete, False)
                    print ('False : La main du joueur fait qu il n est tristan')

            # If test Une carte SANS prophete
            else:
                print'Un joueur a joué une carte!!! '
                print('')

                for x in getCardJson['cards']:

                    carteTmp = Carte(x[0], x[1])

                    print (carteTmp.symbole, carteTmp.valeur , ' : Carte tmp')

                    print ('')

                    # On set les regles
                    setRandomRegle(carteTmp)

                    # Set du return
                    urlValiditeCard = 'http://79.137.38.211/api/public/index.php/card_valid'

                    if nombreRegles == 1:
                        if validiteSuperieur == 1 and validiteInferieur == 1:
                            # requests.post(urlValiditeCard, True)
                            print (x, ' : carte valide')
                        elif validiteCouleur == 1:
                            print ('')
                            #requests.post(urlValiditeCard, True)
                            print (x,' : carte valide')
                        elif validiteParite == 1:
                            #requests.post(urlValiditeCard, True)
                            print (x, ' : carte valide')
                        elif validiteEgalite == 1:
                            # requests.post(urlValiditeCard, True)
                            print (x, ' : carte valide')
                        else:
                            print ('NOPE : carte non valide')

                    # Bool de traitement de plusieurs regles
                    cardValid = 1

                    if nombreRegles == 2:
                        for x in listRegleActive:
                            if x == 'parite':
                                if validiteParite == 1:
                                    # requests.post(urlValiditeCard, True)
                                    print (x, ' : carte valide')
                                else:
                                    cardValid = 0
                                    break
                            elif x == 'couleur':
                                if validiteCouleur == 1:
                                    # requests.post(urlValiditeCard, True)
                                    print (x, ' : carte valide')
                                else:
                                    cardValid = 0
                                    break
                            elif x == 'egalite':
                                if validiteEgalite == 1:
                                    # requests.post(urlValiditeCard, True)
                                    print (x, ' : carte valide')
                                else:
                                    cardValid = 0
                                    break
                            elif x == 'infsup':
                                if validiteInferieur == 1 and validiteSuperieur == 1:
                                    # requests.post(urlValiditeCard, True)
                                    print (x, ' : carte valide')
                                else:
                                    cardValid = 0
                                    break

                        if cardValid == 0:
                            print ('NOPE : une ou plusieurs des regles (2) est fausse')
                        elif cardValid == 1:
                            print ('YES : la carte est valide pour les deux regles') # TODO: TELL APIIIIII POST

                    if nombreRegles == 3:
                        for y in listRegleActive:
                            if y == 'parite':
                                if validiteParite == 1:
                                    # requests.post(urlValiditeCard, True)
                                    print (y, ' : carte valide')
                                else:
                                    cardValid = 0
                                    break
                            elif y == 'couleur':
                                if validiteCouleur == 1:
                                    # requests.post(urlValiditeCard, True)
                                    print (y, ' : carte valide')
                                else:
                                    cardValid = 0
                                    break
                            elif y == 'egalite':
                                if validiteEgalite == 1:
                                    # requests.post(urlValiditeCard, True)
                                    print (y, ' : carte valide')
                                else:
                                    cardValid = 0
                                    break
                            elif y == 'infsup':
                                if validiteInferieur == 1 and validiteSuperieur == 1:
                                    # requests.post(urlValiditeCard, True)
                                    print (y, ' : carte valide')
                                else:
                                    cardValid = 0
                                    break

                        if cardValid == 0:
                            print ('NOPE : une ou plusieurs des regles (3) est fausse')
                        elif cardValid == 1:
                            print ('YES : la carte est valide pour les trois regles') # TODO: TELL APIIIIII POST

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
            getIfCardPlayed = json.loads(reqGetSpamTurn.text)
            if getIfCardPlayed['nouveauCoup'] == 1:
                isCardPlayedValidAndMaybeProphete()