# -*- coding: cp1252 -*-
## \file maladie.py
## \brief Maladies chez l'enfant
## \package maladie
## \brief Maladies chez l'enfant

#1 >  AS COEUR
#2 >  Dame Pique
#3 >  9 de carreaux
#4 >  10 de trefle
#5 >  3 de coeur
#6 >  4 de coeur
#7 >  4 de trefle
#8 >  4 de carreaux

from maladie import*;

# initialise ID3
initID3([
            ['1' , 'coeur', 'rouge', 'impair', 'nontete', 'non'],
            ['12', 'pique', 'noir', 'pair', 'ouitete', 'non'],
            ['9' , 'carreaux', 'rouge', 'impair', 'nontete', 'oui'],
            ['10', 'coeur', 'noir', 'pair', 'nontete', 'nan'],
            ['3' , 'coeur', 'rouge', 'impair', 'nontete', 'non'],
            ['4',  'coeur', 'rouge', 'pair', 'nontete', 'non'],
            ['4',  'trefle', 'noir',  'pair', 'nontete', 'non'],
            ['4',  'carreaux', 'noir', 'pair', 'nontete', 'oui'],
            ['5', 'carreaux', 'noir', 'impair', 'nontete', 'oui'],
            ['6', 'carreaux', 'noir', 'pair', 'nontete', 'oui'],
            ['7', 'carreaux', 'noir', 'impair', 'nontete', 'oui'],
            ['8', 'carreaux', 'noir', 'pai', 'nontete', 'oui']
        ],
        [
            ['valeur', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],
            ['attribut', 'trefle', 'carreaux', 'coeur', 'pique'],
            ['couleur', 'noir', 'rouge'],
            ['parite', 'pair', 'impair'],
            ['tete', 'ouitete', 'nontete'],
            ['resultat', 'oui', 'non']
        ])

# construit l'arbre de décision
construitArbreDecision()