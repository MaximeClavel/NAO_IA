# coding: utf-8

from math import *

class Carte: # Définition de notre classe Carte
    """

    Classe définissant une carte du jeu d'Eleusis par :
    - sa couleur
    - sa valeur

    ##ATTRIBUT##
	#O:Trefle
	#1:Carreaux
	#2:Coeur
	#3:Pique

    ##TETE##
	#11:Vallet
	#12:Dame
	#13:Roi

    """

    def __init__(self, P_attribut, P_valeur): # Notre méthode constructeur
        
        self.attribut = P_attribut #TREFLE, CARREAUX, COEUR, PIQUE
        
        self.valeur = P_valeur     #1, 2, 3, ... , 11, 12, 13
        

        """  Permet de définir la couleur de la carte en fonction de son attribut """
        if self.attribut == 0 or self.attribut == 3:
            self.couleur = 0 #Carte Noir
        else:
            self.couleur = 0 #Carte Rouge

        """  Permet de définir la parité """
        if int(self.valeur)%2 == 0:
            self.parite = 0 #Pair
        else:
            self.parite = 1 #Impair

