# coding: utf-8

from math import *

class Carte: # Définition de notre classe Carte
    """

    Classe définissant une carte du jeu d'Eleusis par :
    - sa couleur
    - sa valeur

    ##SYMBOLE##
	#O:Trefle
	#1:Carreaux
	#2:Coeur
	#3:Pique

    ##TETE##
	#11:Vallet
	#12:Dame
	#13:Roi

    ##COULEUR##
	#0:NOIR
	#1:ROUGE

    ##VALIDE
    # -1 : Pas utilisé
    # 1 : Valide (carte dans liste vrai)
    # 0 : Pas Valide (carte dans liste faux)

    ##POIDS 
    # -1 : Carte à jouer peut - etre 
    #  0 : Carte à ne pas jouer
    #  1 : Carte à jouer impérativement

    """

    def __init__(self, P_symbole, P_valeur): # Notre méthode constructeur
        
        self.symbole = P_symbole #TREFLE, CARREAUX, COEUR, PIQUE
        
        self.valeur = P_valeur     #1, 2, 3, ... , 11, 12, 13
        

        """  Permet de définir la couleur de la carte en fonction de son symbole """
        if self.symbole == 0 or self.symbole == 3:
            self.couleur = 0 #Carte Noir
        else:
            self.couleur = 1 #Carte Rouge

        """  Permet de définir la parité """
        if int(self.valeur)%2 == 0:
            self.parite = 0 #Pair
        else:
            self.parite = 1 #Impair

        if int(self.valeur) > 10:
            self.tete = 1
        else:
            self.tete = 0

        self.valide = -1

        self.poids = -1


    def getValueForAttribute(self, P_attribut):

        return {
          'symbole': self.symbole,
          'valeur': self.valeur,
          'couleur': self.couleur,
          'parite':self.parite,
          'tete': self.tete,
          'valide':self.valide,

        }[P_attribut]







