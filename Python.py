# coding: utf-8

#Projet IA

import requests
import json
from Carte import Carte

maCarte = Carte(0,8)

url = 'http://79.137.38.211/api/public/index.php/'

url_jouerCoup='jouercoup'


#carte : [int couleur, int rank]

Hand = getHand()



#***JOUER UNE CARTE ****#
#playcard = {'card': [maCarte.color,maCarte.value]}
#reqPost = requests.post(url+url_jouerCoup, json=playcard)








#***** GET DES CARTES QUE L'ON A DANS LA MAIN *****#
def getHand():
	#reqGetHand = requests.get('http://79.137.38.211/api/public/index.php/gethand')
	reqGetHand = requests.get('http://echo.jsontest.com/couleur/mesboules/Tristal/LeCristal')
	with open(reqGetHand) as data_hand :
		handJson = json.load(data_hand)
	print(handJson)
	return handJson



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