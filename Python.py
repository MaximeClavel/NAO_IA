# coding: utf-8

#Projet IA
# turn 4 : IA
# turn 0 : Prophete
# turn -1 : Attente

import requests
import os
import json
from Carte import Carte


clear = lambda: os.system('clear')

#********FONCTIONS********#

#** GET BEST CARD **#
def getBestCard(HandJson,index):

	##** ARBRE DE DECISION **##

	#carteAjouer = Carte(0,9)

	tabHand = HandJson['hand']
	print tabHand
	for i in range(0,5):
		print tabHand[i] #Ceci affiche chaque carte de la main
		print tabHand[i][0] #COULEUR DE LA CARTE
		print tabHand[i][1]	#NUMERO DE LA CARTE

	"""
	with HandJson['hand'] as data_hand :
		CardJson = json.load(data_hand)
		print(CarJson.text)
	"""

	carteAjouer = Carte(tabHand[index][0],tabHand[index][1])

	return carteAjouer



#** JOUER CARTE**#
def jouerCoup(CarteAjouer,monprint):
	
	#monprint += 'AVANT ENVOI CarteCouleur :' + str(CarteAjouer.color) + ' CarteValeur :' + str(CarteAjouer.value)
	playcard = {'card_to_play': [CarteAjouer.color,CarteAjouer.value]}
	reqPost = requests.post(url+url_jouerCoup, json=playcard)
	
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

#** GET INFOS**#
#Récupérer les cartes de notre mains, et les listes Vrai Faux
#Compléter l'objet de la carte

def getHand():
	
	monprint = ''
	index = 0

	while True:

		reqGetHand = requests.get(url+url_getHand)
		"""
		print''
		print'reqGetHand :'
		print reqGetHand
		print'reqGetHand.text :'
		print reqGetHand.text
		print''
		"""
		
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
				
				"""print''
				print getHandJson

				print getHandJson
				print''
				print 'DUMPS'
				json.dumps(getHandJson, sort_keys=True, indent=2)
				
				print''
				print'Données récupérées : '
				print getHandJson.text

				print''
				print'DECODED'
				print getHandJson['truth_list']

				print''
				print'TEXT'"""

				#Lancer la fonction d'arbres décisionnel ici
				#Si c'est à nous de jouer alors
				
				carteAJouer = getBestCard(getHandJson,index)
				index += 1

				jouerCoup(carteAJouer,monprint)

				print''
				monprint += 'Carte joué : ' + ' Color=' + str(carteAJouer.color) + ' & Value=' + str(carteAJouer.value) + '\r\n'
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

	url = 'http://79.137.38.211/api/public/index.php/'

	url_jouerCoup='jouercoup'
	url_getHand='gethand'

	print''
	print'Get Hand'
	print''
	#Récupère les carte et joue le coup lorsque c'est à nous de jouer
	getHand()

	print '######## FIN DU PROGRAMME ########'







"""
r = requests.get('http://echo.jsontest.com/events/mesboules/Tristal/LeCristal')
print(r.text)

r = requests.get('http://79.137.38.211/api/public/index.php/hello/maxime')
print(r.text)

print(maCarte.color)
print(maCarte.value)

print('')
print('playcard : ')
print(playcard)



print('')
print('***POST***')

print('')
print('print text : ')
print(r.text)
print('')
print('print json : ')
print(r.json())
print('')
print('print réponse : ')
print(r)
print('')
"""