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
from Arbre import *
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
def getBestCard(index, ListeMain):


	##** ARBRE DE DECISION **##

	#carteAjouer = Carte(0,9)

	#TabCartesVrai à passer à l'arbre
	tabCartesVrai = []
	tabCartesFaux = []

	tailleTabVrai = len(gListeVrai)
	tailleTabFaux = len(gListeFaux)

	print 'Ma main'
	print ListeMain
	print ''

	for i in range(0,5):
		print ListeMain[i] 	#Ceci affiche chaque carte de la main
		print ListeMain[i][0]	#SYMBOLE DE LA CARTE
		print ListeMain[i][1]	#NUMERO DE LA CARTE


	#On rempli un tablaeu d'instance de carte suivant les tableaux reçus depuis l'API
	for j in range(0,tailleTabVrai):
		carteVrai = Carte(gListeVrai[j][0], gListeVrai[j][1]) #SYMBOLE DE LA CARTE, NUMERO DE LA CARTE
		tabCartesVrai.append(carteVrai)

	for k in range(0,tailleTabFaux):
		carteFaux = Carte(gListeFaux[k][0], gListeFaux[k][1]) #SYMBOLE DE LA CARTE, NUMERO DE LA CARTE
		tabCartesFaux.append(carteFaux)


	monArbre = Arbre(tabCartesVrai, tabCartesFaux)

	print 'TEST de la carte ' + str(ListeMain[0])
	monArbre.testCarte(ListeMain[0])


	sleep(15)

	"""
	with HandJson['hand'] as data_hand :
		CardJson = json.load(data_hand)
		print(CarJson.text)
	"""

	#carteAjouer = Carte(tabHand[index][0],tabHand[index][1])

	return carteAjouer



#** JOUER CARTE**#
def jouerCoup(CarteAjouer):
	
	global monprint

	monprint += 'AVANT ENVOI CarteCouleur :' + str(CarteAjouer.symbole) + ' CarteValeur :' + str(CarteAjouer.valeur)
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

			if getHandJson['turn'] == '0':
				
				print''
				print'Someone is PROPHETE'
				return

			#if getHandJson['turn'] == '4':
			print''
			print 'A nous de jouer !'
			
			#Récupération de la liste main
			gListeMain = getHandJson['hand']
			print gListeMain
			#Récupération de la liste vrai
			gListeVrai = getHandJson['truth_list']
			#Récupération de la liste faux
			gListeFaux = getHandJson['wrong_list']

			#concatListes(gListeVrai,gListeFaux)

			#Lancer la fonction d'arbres décisionnel ici
			#Si c'est à nous de jouer alors
			#Arbre de décision à lancer
			carteAJouer = getBestCard(index, gListeMain)
			index += 1#randrange(5)

			jouerCoup(carteAJouer)

			print''
			monprint += 'Carte joué : ' + ' attribut=' + str(carteAJouer.attribut) + ' & valeur=' + str(carteAJouer.valeur) + '\r\n'
			print monprint

		else:
			print''
			print('Reponse ' + str(reqGetHand.status_code) + ' du serveur.')
"""
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

"""
			
		
						
				
 

def test():
	"Fonction de test."
	maFonction = maFonction +1
	return maFonction


#********************************************#
#******************* MAIN *******************#
#*******carte: [int couleur, int rank]*******#
#********************************************#

if __name__ == '__main__':

	print '######## DEBUT DU PROGRAMME ########'
	maCarte = Carte(0,6)
	maCarte2 = Carte(3,4)
	maCarte3 = Carte(2,8)
	maCarte4 = Carte(1,7)
	#gListeMain.append(maCarte)

	#print gListeMain
	print''

	montab = ['Tete','tab','mesboules']
	montabCarte = [maCarte, maCarte2, maCarte3, maCarte4]

	url='http://79.137.38.211/api/public/index.php/'
	url_jouerCoup='jouercoup'
	url_getHand='gethand'

	print''
	print'Get Hand'
	print''
	
	#TODO : 
	#filtre tableau 
	#donc tableau manquant gethigherpert,...
	#Faire des cartes 


	#monArbre = Arbre()


	#Récupère les carte et joue le coup lorsque c'est à nous de jouer
	getHand()

	#print 'Valeur de la tete de ma carte : ' + str(maCarte.getValueForAttribute('tete'))

	""""
	print 'Tableau : ' + str(montabCarte)

	for x in range(0,len(montabCarte)):
		print 'Carte : tete=' + str(montabCarte[x].tete) + ' symbole=' + str(montabCarte[x].symbole) + ' valeur=' + str(montabCarte[x].valeur)
		if montabCarte[x].tete == 0:
			print 'Carte Delete : symbole=' + str(montabCarte[x].symbole) +' valeur=' + str(montabCarte[x].valeur)
			montabCarte.remove(montabCarte[x])


	print 'Tableau sorti : ' + str(montabCarte)
	"""

	#print test.__doc__
	print ''

	print '######## FIN DU PROGRAMME ########'

