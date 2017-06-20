# coding: utf-8

#Projet IA

import requests
import json
from Carte import Carte

#r = requests.get('http://echo.jsontest.com/events/mesboules/Tristal/LeCristal')
#print(r.text)

#r = requests.get('http://79.137.38.211/api/public/index.php/hello/maxime')
#print(r.text)

maCarte = Carte(0,8)

url = 'http://79.137.38.211/api/public/index.php/'

url_jouerCoup='jouercoup'

#***** AJOUTER UNE CLASSE POUR CARTE *****#
#carte : [int couleur, int rank]

print(maCarte.color)
print(maCarte.value)

playcard = {'card': '[' + str(maCarte.color) + ',' + str(maCarte.value) +']'}

print('playcard : ')
print(playcard)

#***** GET DES CARTES QUE L'ON A DANS LA MAIN *****#
r = requests.post(url+url_jouerCoup, data=playcard)

print('print text : ')
print(r.text)
print('print json : ')
print(r.json())
print('print réponse : ')
print(r)