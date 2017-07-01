# coding: utf-8

from math import *

class Arbre:

    def __init__(self, exemplesVrai, exemplesFaux):
        
        self.monNoeud = Noeud

        self.tabNoeudPossible = ['tete','valeur','parite','couleur','symbole']

        self.exemplesVrai = exemplesVrai
        self.exemplesFaux = exemplesFaux

        # [Valeur, Attribut, Parite, Tete, Couleur, Bonne carte]
        # Huit de carreau qui est passe [8, 1, 1, 0, 0, 1]
        # Roi de trèfle qui ne passe pas [13, 0, 0, 1, 0, 0]

        tailleVrai = len(exemplesVrai)
        tailleFaux = len(exemplesFaux)
        sommeTab = tailleVrai + tailleFaux
        
        #self.EntropieValide = - tailleVrai/sommeTab*log(tailleVrai/sommeTab,2) - tailleFaux/sommeTab * log(tailleFaux/sommeTab,2)

        self.tabVraiCourant = exemplesVrai

        self.tabFauxCourant = exemplesFaux

        self.noeudCourant = 'root'
        self.valueNoeudCourant = 0.0

    def calculProbabilite(self, attributCard, valeur):
    	pOui = 0.0
    	pNon = 0.0


        
        for cV in listCardVrai:
			if cV.getValueForAttribute(attributCard) == valeur and cV.getValueForAttribute(currentNode) == currentNodeValue or currentNode == 'root'
            	pOui++

        for cF in listCardFaux:
        	if cF.getValueForAttribute(attributCard) == valeur and cF.getValueForAttribute(currentNode) == currentNodeValue or currentNode == 'root' 
            	pNon++
                            
        
        array = []
        array.append(pOui)
        array.append(pNon)

        return array
    
    def calculEntropie(self, pOui, pNon):
        nbTotal = pOui + pNon
        return (-pOui/nbTotal) * log(pOui/nbTotal, 2) - (pNon/nbTotal) * log(pNon/nbTotal, 2)

    def calculPertinence(self, attribut, nbValuesPossible):

        sommeTabCourant = len(self.tabVraiCourant) + len(self.tabFauxCourant)
        pertinence = - len(self.tabVraiCourant)/sommeTabCourant*log(len(self.tabVraiCourant)/sommeTabCourant,2) - len(self.tabFauxCourant)/sommeTabCourant * log(len(self.tabFauxCourant)/sommeTabCourant,2)

        #Tableau de tableau double [[1.0, 2.0], [2.5, 4.2]] tabPertinenceValue

        tabPertinenceValue = []

        for i in range(0,nbValuesPossible):
            tabPertinenceValue.append(calculEntropieAttribut(attribut, i))
        

        #pertinence = self.EntropieValide;

        for j in range(0,nbValuesPossible):

            pertinence = pertinence - ( (tabPertinenceValue[j][0] + tabPertinenceValue[j][1]) / (len(self.tabVraiCourant)+len(self.tabFauxCourant)) ) * calculEntropie(tabPertinenceValue[j]);
        
        return pertinence

    

    def switchPossibleNode(attribut):
        return {
          'symbole': 4,
          'valeur': 13,
          'couleur': 2,
          'parite':2,
          'tete': 2,
        }[attribut]



    def getHigherPertinence(self):
        if len(self.tabNoeudPossible) > 0:

            pertinence = tabNoeudPossible[0]
            
            higherPert = calculPertinence(pertinence, switchPossibleNode(pertinence))

            for element in tabNoeudPossible:
                if element != pertinence:
                    pert = calculPertinence(element,switchPossibleNode(element))

                    if pert > higherPert:
                        higherPert = pert
                        pertinence = element
        
            return pertinence
        else
            return ''

    def isLeaf(self, attribut, valeur):
        leaf = 0
        arr = calculProbabilite(attribut, valeur);
        pOui = arr[0]
        pNon = arr[1]
        
        if pOui > 0.0 and pNon == 0.0 :
            leaf = 1
            for i in  range(0,level):

                #Level deep
        
        elif pOui == 0.0 and pNon > 0.0:

            leaf = 1
            for i in  range(0,level):
               #Level deep
        if leaf = 0
            self.valueNoeudCourant = valeur
            self.NoeudCourant = attribut
        
        return leaf





    def recursivite():
        return














