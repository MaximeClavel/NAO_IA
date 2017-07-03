# coding: utf-8

from math import *
from NoeudPierre import *

class Arbre:

    def __init__(self, tabVrai, tabFaux):
        self.noeud = Noeud('root')
        self.noeudCourant = Noeud('root')
        self.valeurCourante = 0
        self.isRoot = 1

        self.tabVrai = tabVrai
        self.tabFaux = tabFaux
        self.possibleNodes = ['parite', 'tete', 'couleur', 'symbole']

    #Calcule l'entropie
    #pOui est la probabilité de Oui
    #pNon est la probabilité de Non
    def calculEntropie(self, pOui, pNon):
        return -(pOui) * log(pOui, 2) - pNon * log(pNon, 2)


    def switchPossibleNode(self, attribut):
        return {
          'symbole': 4,
          'valeur': 13,
          'couleur': 2,
          'parite': 2,
          'tete': 2,
        }[attribut]


    def calculPertinence(self, attribut, tabVrai, tabFaux):
        "Entropie(Attribut) - Somme des Proportions d'exemples ayant une valeur donnée multipliées par l'entropie pour chaque valeur"

        baseVrai = len(tabVrai)
        baseFaux = len(tabFaux)
        baseTotal = (baseVrai + baseFaux) * 1.0
        base = self.calculEntropie((baseVrai/baseTotal), (baseFaux/baseTotal))

        lengthAttribute = self.switchPossibleNode(attribut)
        somme = 0.0
        for j in range(0, lengthAttribute):

            nbOfValueOfAttribute = 0
            nbValueVraiOfAttribute = 0
            nbValueFauxOfAttribute = 0
            for i in tabVrai:
                if i.getValueForAttribute(attribut) == j:
                    nbOfValueOfAttribute = nbOfValueOfAttribute + 1
                    nbValueVraiOfAttribute = nbValueVraiOfAttribute + 1

            for k in tabFaux:
                if k.getValueForAttribute(attribut) == j:
                    nbOfValueOfAttribute = nbOfValueOfAttribute + 1
                    nbValueFauxOfAttribute = nbValueFauxOfAttribute + 1

            nbOfValueOfAttribute = nbOfValueOfAttribute * 1.0
            nbValueVraiOfAttribute = nbValueVraiOfAttribute * 1.0
            nbValueFauxOfAttribute = nbValueFauxOfAttribute * 1.0
            if nbOfValueOfAttribute > 0.0 and nbValueVraiOfAttribute > 0.0 and nbValueFauxOfAttribute > 0.0:
                somme = somme + (nbOfValueOfAttribute/baseTotal) * self.calculEntropie((nbValueVraiOfAttribute/nbOfValueOfAttribute), (nbValueFauxOfAttribute/nbOfValueOfAttribute))
        return base - somme


    def getHighestPertinence(self, tabVrai, tabFaux, possibleNodes):
        if len(possibleNodes) > 0:
            highestPert = self.calculPertinence(possibleNodes[0], tabVrai, tabFaux)
            pert = possibleNodes[0]

            for i in possibleNodes:
                if i != pert:
                    testPert = self.calculPertinence(i, tabVrai, tabFaux)
                    if testPert > highestPert:
                        highestPert = testPert
                        pert = i

            possibleNodes.remove(pert)
        else:
            pert = ''
        return [pert, possibleNodes]


    def filter(self, ptableau, attribut, valeur):
        "Retourne un tableau qui garde seulement les cartes qui on la valeur 'valeur' pour leur attribut 'attribut'"

        tableau = ptableau

        if attribut != 'root':
            tailleTab = len(tableau)

            if attribut == 'tete':
                x = 0
                while x < len(tableau):
                    if tableau[x].tete != valeur:
                        tableau.remove(tableau[x])
                        x = x - 1
                    x = x + 1

            if attribut == 'symbole':
                x = 0
                while x < len(tableau):
                    if tableau[x].symbole != valeur:
                        tableau.remove(tableau[x])
                        x = x - 1
                    x = x + 1

            if attribut == 'valeur':
                x = 0
                while x < len(tableau):
                    if tableau[x].valeur != valeur:
                        tableau.remove(tableau[x])
                        x = x - 1
                    x = x + 1

            if attribut == 'couleur':
                x = 0
                while x < len(tableau):
                    if tableau[x].couleur != valeur:
                        tableau.remove(tableau[x])
                        x = x - 1
                    x = x + 1

            if attribut == 'parite':
                x = 0
                while x < len(tableau):
                    if tableau[x].parite != valeur:
                        tableau.remove(tableau[x])
                        x = x - 1
                    x = x + 1

        return tableau


    def hasValue(self, array, attribut, valeur):
        for carte in array:
            if carte.getValueForAttribute(attribut) == valeur:
                return 1

        return 0


    def construire(self, tabVrai, tabFaux, attribut, valeur, noeudsPossibles, parent):
        print 'Valeur : ' + str(valeur )
        arrayTrue = self.filter(tabVrai, attribut, valeur)
        arrayFalse = self.filter(tabFaux, attribut, valeur)
        # Si le noeud courant est terminal on set le noeud en tant que feuille et on return
        if self.noeudCourant.isTerminal(arrayTrue, arrayFalse) == 1:
            print 'attribut : ' + attribut
            noeudTmp = Noeud(attribut)
            noeudTmp.isLeaf = 1
            if len(arrayTrue) > 0:
                noeudTmp.resultat = 1
            else:
                noeudTmp.resultat = 0
            tabTmp = [valeur, noeudTmp]
            print 'Fin isTerminal --- isLeaf => ' + str(noeudTmp.isLeaf) + ' --- resultat => ' + str(noeudTmp.resultat)
            self.noeudCourant.children.append(tabTmp)
            print 'Feuille trouvée'
            self.noeudCourant = parent
        else:
            # Créer un noeud et continuer l'algorithme
            tabPertinence = self.getHighestPertinence(tabVrai, tabFaux, noeudsPossibles)
            pertinence = tabPertinence[0]
            if len(tabPertinence[1]) == 0:
                return
            if self.isRoot == 1:
                self.noeud = Noeud(pertinence)
                self.noeudCourant = self.noeud
                parent = self.noeudCourant
                print 'Racine créée avec attribut : ' + pertinence
                self.isRoot = 0
            else:
                noeudTmp = Noeud(pertinence)
                tabTmp = [valeur, noeudTmp]
                self.noeudCourant.children.append(tabTmp)
                parent = self.noeudCourant
                self.noeudCourant = self.noeudCourant.children[len(self.noeudCourant.children) - 1][1]
                print 'Noeud créé avec attribut : ' + pertinence

            # Pour toutes les valeurs existantes dans les exemples de l'attribut considéré comme pertinent
            # Construire la suite
            length = self.switchPossibleNode(pertinence)

            for i in range(0, length):
                arrayTrueTmp = []
                for elem in arrayTrue:
                    arrayTrueTmp.append(elem)
                arrayFalseTmp = []
                for elemFalse in arrayFalse:
                    arrayFalseTmp.append(elemFalse)
                arrayPossibleNodesTmp = []
                for elemNodes in tabPertinence[1]:
                    arrayPossibleNodesTmp.append(elemNodes)

                if self.hasValue(arrayTrueTmp, pertinence, i) == 1:
                    self.construire(arrayTrueTmp, arrayFalseTmp, pertinence, i, arrayPossibleNodesTmp, parent)
                elif self.hasValue(arrayFalseTmp, pertinence, i) == 1:
                    self.construire(arrayTrueTmp, arrayFalseTmp, pertinence, i, arrayPossibleNodesTmp, parent)
        print 'Fin de fonction'

    def testCarte(self, carte):
        self.noeud.testCarte(carte)
