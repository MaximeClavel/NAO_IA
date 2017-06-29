# coding: utf-8

#Projet IA
# turn 4 : IA
# turn 0 : Prophete
# turn -1 : Attente

#turn , hand, truth_list, wrong_list

import requests
import os
import json
from Carte import *
from random import *
#from Liste import *

gListeMain=[]
gListeVrai=[]
gListeFaux=[]

monprint=''

clear = lambda: os.system('clear')




#********FONCTIONS********#

#def concatListes(P_ListeVrai, P_ListeFaux):

	#for i in range(0,52):
	#P_ListeVrai



#** GET BEST CARD **#
def getBestCard(index):

	##** ARBRE DE DECISION **##

	#carteAjouer = Carte(0,9)

	

	print gListeMain

	for i in range(0,5):
		print gListeMain[i] 	#Ceci affiche chaque carte de la main
		print gListeMain[i][0]	#ATTRIBUT DE LA CARTE
		print gListeMain[i][1]	#NUMERO DE LA CARTE

	"""
	with HandJson['hand'] as data_hand :
		CardJson = json.load(data_hand)
		print(CarJson.text)
	"""

	carteAjouer = Carte(tabHand[index][0],tabHand[index][1])

	return carteAjouer



#** JOUER CARTE**#
def jouerCoup(CarteAjouer):
	
	global monprint

	monprint += 'AVANT ENVOI CarteCouleur :' + str(CarteAjouer.attribut) + ' CarteValeur :' + str(CarteAjouer.valeur)
	playcard = {'card_to_play': [CarteAjouer.attribut,CarteAjouer.valeur]}
	reqPost = requests.post(url+url_jouerCoup, json=playcard)
	
	"""
	print''
	print ("JSON :")
	print(reqPost.text)
	print''
	print ("STATUS :")
	print(reqPost.status_code)
	print''
	print("URL :")
	print(url+url_jouerCoup)
	print''

	"""

#** GET INFOS**#
#Récupérer les cartes de notre mains, et les listes Vrai Faux
#Compléter l'objet de la carte

def getHand():
	
	global monprint
	index = 0

	while True:

		reqGetHand = requests.get(url+url_getHand)

		
		if reqGetHand.status_code == 200:

			getHandJson = json.loads(reqGetHand.text)
			#print reqGetHand.text

			if getHandJson['turn'] == 0:
				
				print''
				print'Someone is PROPHETE'
				return

			if getHandJson['turn'] == '4':
				print''
				print 'A nous de jouer !'
				
				#Récupération de la liste main
				gListeMain = getHandJson['hand']
				#Récupération de la liste vrai
				gListeVrai = getHandJson['truth_list']
				#Récupération de la liste faux
				gListeFaux = getHandJson['wrong_list']

				concatListes(gListeVrai,gListeFaux)

				#Lancer la fonction d'arbres décisionnel ici
				#Si c'est à nous de jouer alors
				#Arbre de décision à lancer
				carteAJouer = getBestCard(index)
				index += 1#randrange(5)

				jouerCoup(carteAJouer)

				print''
				monprint += 'Carte joué : ' + ' attribut=' + str(carteAJouer.attribut) + ' & valeur=' + str(carteAJouer.valeur) + '\r\n'
				print monprint

			elif getHandJson['turn'] == -1:
				clear()
				print monprint
				print ''
				print 'A personne de jouer...'		
			else:
				
				clear()
				print monprint
				print ''
				print 'En attente de notre tour...'


			

		else:
				print''
				print('Reponse ' + str(reqGetHand.status_code) + ' du serveur.')				
				
 




#********************************************#
#******************* MAIN *******************#
#*******carte: [int couleur, int rank]*******#
#********************************************#

if __name__ == '__main__':

	
	maCarte = Carte(0,8)

	gListeMain.append(maCarte)

	print gListeMain
	print''



	url='http://79.137.38.211/api/public/index.php/'
	url_jouerCoup='jouercoup'
	url_getHand='gethand'

	print''
	print'Get Hand'
	print''
	


	#monArbre = Arbre()


	#Récupère les carte et joue le coup lorsque c'est à nous de jouer
	getHand()

	print '######## FIN DU PROGRAMME ########'

