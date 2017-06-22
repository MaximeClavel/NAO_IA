# coding: utf-8

#Projet IA

import requests
import json
from Carte import Carte

#********FONCTIONS********#

#** GET INFOS**#
#Récupérer les cartes de notre mains, et les listes Vrai Faux
#Compléter l'objet de la carte

def getHand():
	
	reqGetHand = requests.get(url+url_getHand)
	print''
	print'reqGetHand :'
	print reqGetHand
	print'reqGetHand.text :'
	print reqGetHand.text
	print''
	getHandJson = json.loads(reqGetHand.text)

	while getHandJson['turn'] != 4:
		print''
		print'Turn :'
		print getHandJson['turn']

		reqGetHand = requests.get(url+url_getHand)
		#reqGetHand = requests.get('http://echo.jsontest.com/couleur/mesboules/Tristal/LeCristal')
		print''
		print getHandJson

		print''
		getHandJson = json.loads(reqGetHand.text)

		print getHandJson
		print''
		print 'DUMPS'
		print json.dumps(getHandJson, sort_keys=True, indent=4)

		print''
		print'DECODED'
		print getHandJson['truth_list']

		print''
		print'TEXT'
		print(reqGetHand.text)

		#with open(reqGetHand) as data_hand :
			#handJson = json.load(data_hand)
		#print(handJson)


	return getHandJson #reqGetHand

	


#** JOUER CARTE**#
def jouerCoup(CarteAjouer):
	playcard = {'card': [CarteAjouer.color,CarteAjouer.value]}
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


#********************************************#
#******************* MAIN *******************#
#*******carte: [int couleur, int rank]*******#
#********************************************#

if __name__ == '__main__':

	maCarte = Carte(0,8)

	url = 'http://79.137.38.211/api/public/index.php/'

	url_jouerCoup='jouercoup'
	url_getHand='gethand'

	
	#jouerCoup(maCarte)
	getHand()









#******* FONCTION SPAM **********#
#a moi ? (tourjoueur à moi ?)
#Oui maj de la main + Listes vrai/faux(dans tab)
#Classe Main, ListeVraiFaux








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