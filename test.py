# -*- coding: cp1252 -*-
## \file maladie.py
## \brief Maladies chez l'enfant
## \package maladie
## \brief Maladies chez l'enfant
from maladie import*;

# initialise ID3
initID3([['angine-erythemateuse', 'elevee', 'gonflees', 'oui', 'oui', 'non', 'non', 'non', 'normale', 'normales','normaux'],
         ['angine-pultacee', 'elevee', 'points-blancs', 'oui', 'oui', 'non', 'non', 'non', 'normale', 'normales','normaux'],
         ['angine-diphterique', 'legere', 'enduit-blanc', 'oui', 'oui', 'non', 'non', 'non', 'normale', 'normales','normaux'],
         ['appendicite', 'legere', 'normales', 'non', 'non', 'oui', 'non', 'non', 'normale', 'normales', 'normaux'],
         ['bronchite', 'legere', 'normales', 'oui', 'non', 'non', 'oui', 'oui', 'genee', 'normales', 'normaux'],
         ['coqueluche', 'legere', 'normales', 'non', 'oui', 'non', 'oui', 'oui', 'genee', 'normales', 'normaux'],
         ['pneumonie', 'elevee', 'normales', 'non', 'non', 'non', 'oui', 'non', 'rapide', 'rouges', 'normaux'],
         ['rougeole', 'legere', 'normales', 'non', 'oui', 'non', 'oui', 'oui', 'normale', 'normales', 'larmoyants'],
         ['rougeole', 'legere', 'normales', 'non', 'oui', 'non', 'oui', 'oui', 'normale', 'taches-rouges','larmoyants'],
         ['rubeole', 'legere', 'normales', 'oui', 'non', 'non', 'non', 'non', 'normale', 'taches-rouges', 'normaux'],
         ['rubeole', 'non', 'normales', 'oui', 'non', 'non', 'non', 'non', 'normale', 'taches-rouges', 'normaux'],
         ['rubeole', 'non', 'normales', 'oui', 'non', 'non', 'non', 'non', 'normale', 'normales', 'normaux']],

        [['maladies', 'angine-erythemateuse', 'angine-pultacee', 'angine-diphterique', 'appendicite', 'bronchite','coqueluche','pneumonie', 'rougeole', 'rubeole'],
         ['fievre', 'non', 'legere', 'elevee'],
         ['amygdales', 'normales', 'gonflees', 'points-blancs', 'enduit-blanc'],
         ['ganglions', 'non', 'oui'],
         ['gene-a-avaler', 'non', 'oui'],
         ['mal-au-ventre', 'non', 'oui'],
         ['toux', 'non', 'oui'],
         ['rhume', 'non', 'oui'],
         ['respiration', 'normale', 'genee', 'rapide'],
         ['joues', 'normales', 'rouges', 'taches-rouges'],
         ['yeux', 'normaux', 'larmoyants']])

# construit l'arbre de décision
construitArbreDecision()







def filter(self, ptableau, attribut, valeur):

   "Retourne un tableau qui garde seulement les cartes qui on la valeur 'valeur' pour leur attribut 'attribut'"
   
   tableau = ptableau

   tailleTab = len(tableau)

   if attribut == 'tete':
   
      for x in range(0,tailleTab):
         
         if tableau[x].tete != valeur:
            tableau.remove(tableau[x])

   if attribut == 'symbole':

      for x in range(0,tailleTab):
         
         if tableau[x].symbole != valeur:
            tableau.remove(tableau[x])

   if attribut == 'valeur':

      for x in range(0,tailleTab):
         
         if tableau[x].valeur != valeur:
            tableau.remove(tableau[x])

   if attribut == 'couleur':

      for x in range(0,tailleTab):
         
         if tableau[x].couleur != valeur:
            tableau.remove(tableau[x])

   if attribut == 'parite':

      for x in range(0,tailleTab):
         
         if tableau[x].parite != valeur:
            tableau.remove(tableau[x])



   return tableau









