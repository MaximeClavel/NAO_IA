# coding: utf-8

from ArbrePierre import *
from Carte import *

if __name__ == '__main__':
    print ''
    print '######## DEBUT DU PROGRAMME ########'

    maCarte = Carte(0, 6)
    maCarte1 = Carte(2, 6)
    maCarte2 = Carte(1, 13)
    maCarte3 = Carte(0, 7)
    maCarte4 = Carte(3, 12)
    maCarte5 = Carte(0, 10)
    maCarte6 = Carte(1, 8)

    print ''

    print '####### CREATION DE L\'ARBRE ########'
    print ''

    tabVrai = [Carte(0, 11), Carte(3, 9), Carte(3, 3), Carte(0, 10), Carte(0, 1), Carte(3, 1)]
    tabFaux = [Carte(1, 5), Carte(1, 1), Carte(1, 13), Carte(2, 8), Carte(1, 9), Carte(2, 11)]
    arbre = Arbre(tabVrai, tabFaux)

    print '####### ARBRE CREE ########'
    print ''

    print '####### CONSTRUCTION DE L\'ARBRE #######'
    print ''

    possibleNodes = ['parite', 'tete', 'couleur', 'symbole']
    arbre.construire(tabVrai, tabFaux, 'root', 0, possibleNodes)

    print ''
    print '####### ARBRE CONSTRUIT #######'
    print ''

    print '####### TEST DE LA CARTE #######'
    print ''

    arbre.testCarte(maCarte)
    arbre.testCarte(maCarte1)
    arbre.testCarte(maCarte2)
    arbre.testCarte(maCarte3)
    arbre.testCarte(maCarte4)
    arbre.testCarte(maCarte5)
    arbre.testCarte(maCarte6)

    print '####### CARTE TESTEE #######'
    print ''

    print 'Poids : ' + str(maCarte.poids)
    print 'Poids 1: ' + str(maCarte1.poids)
    print 'Poids 2: ' + str(maCarte2.poids)
    print 'Poids 3: ' + str(maCarte3.poids)
    print 'Poids 4: ' + str(maCarte4.poids)
    print 'Poids 5: ' + str(maCarte5.poids)
    print 'Poids 6: ' + str(maCarte6.poids)

    print ''