# coding: utf-8

from math import *

class Arbre:

    def __init__(self, exemples):
        self.exemples = exemples
        # [Valeur, Attribut, Parite, Tete, Couleur, Bonne carte]
        # Huit de carreau qui est passe [8, 1, 1, 0, 0, 1]
        # Roi de trèfle qui ne passe pas [13, 0, 0, 1, 0, 0]

    def calculEntropie(self, pOui, pNon):
        nbTotal = pOui + pNon
        return (-pOui/nbTotal) * log(pOui/nbTotal, 2) - (pNon/nbTotal) * log(pNon/nbTotal, 2)

    def calculPertinance(self):