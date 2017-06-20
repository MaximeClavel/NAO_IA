# coding: utf-8
class Carte: # Définition de notre classe Carte
    """

    Classe définissant une du jeu d'Eleusis par :
    - sa couleur
    - sa valeur

	#O:Trefle
	#1:Carreaux
	#2:Coeur
	#3:Pique

	#11:Vallet
	#12:Dame
	#13:Roi

    """

    def __init__(self, P_color, P_value): # Notre méthode constructeur
        
        self.color = P_color
        self.value = P_value