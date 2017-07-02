# coding: utf-8

from math import *
from Noeud import *

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



    def calculProbabilite(self, attributCard, valeur):
        pOui = 0.0
        pNon = 0.0
        listCardVrai = self.exemplesVrai
        listCardFaux = self.exemplesFaux

        
        for cV in listCardVrai:
            if cV.getValueForAttribute(attributCard) == valeur and cV.getValueForAttribute(currentNode) == currentNodeValue or currentNode == 'root'
                pOui = pOui + 1

        for cF in listCardFaux:
            if cF.getValueForAttribute(attributCard) == valeur and cF.getValueForAttribute(currentNode) == currentNodeValue or currentNode == 'root'
                pNon = pNon + 1
                            
        
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
            tabPertinenceValue.append(calculProbabilite(attribut, i))
        

        #pertinence = self.EntropieValide;

        for j in range(0,nbValuesPossible):

            pertinence = pertinence - ( (tabPertinenceValue[j][0] + tabPertinenceValue[j][1]) / (len(self.tabVraiCourant)+len(self.tabFauxCourant)) ) * calculEntropie(tabPertinenceValue[j]);
        
        return pertinence

    

    def switchPossibleNode(attribut):
        return {
          'symbole': 4,
          'valeur': 13,
          'couleur': 2,
          'parite': 2,
          'tete': 2,
        }[attribut]



    def getHigherPertinence(self):
        if len(self.tabNoeudPossible) > 0:

            pertinence = self.tabNoeudPossible[0]
            
            higherPert = calculPertinence(pertinence, switchPossibleNode(pertinence))

            for element in self.tabNoeudPossible:
                if element != pertinence:
                    pert = calculPertinence(element, switchPossibleNode(element))

                    if pert > higherPert:
                        higherPert = pert
                        pertinence = element

            self.tabNoeudPossible.remove(pertinence)
            return pertinence
        else:
            return ''



    # Valeurs de leaf :
    # -1 : Non valide
    # 0 : Pas une feuille
    # 1 : Une feuille -> Oui
    # 2 : Une feuille -> Non
    def isLeaf(self, attribut, valeur):
        leaf = 0
        arr = calculProbabilite(attribut, valeur)
        pOui = arr[0]
        pNon = arr[1]
        
        if pOui > 0.0 and pNon == 0.0 :
            leaf = 1
        elif pOui == 0.0 and pNon > 0.0:
            leaf = 2
        elif pOui == 0.0 and pNon == 0.0:
            leaf = -1

        if leaf == 0:
            self.valueNoeudCourant = valeur
            self.noeudCourant = attribut
        
        return leaf



    def calculNode(self, attribut, valeur, noeudPrecedent):
        self.valueNoeudCourant = valeur
        self.noeudCourant = attribut
        s = getHigherPertinence()
        if self.noeudCourant == 'root':
            self.monNoeud = Noeud('', attribut, 0, 0)
        #On devrait avoir des conditions ici pour la valeur de s

        length = switchPossibleNode(s)
        if s == 'valeur':
            for i in range(1, length + 1):
                leaf = isLeaf(s, i)
                if leaf == 0:
                    tab = [valeur, Noeud(noeudPrecedent, attribut, 0, 0)]
                    noeudPrecedent.tabShield.append(tab)
                    calculNode(s, i)
                elif leaf == 1:
                    tab = [valeur, Noeud(noeudPrecedent, attribut, 1, 1)]
                    noeudPrecedent.tabShield.append(tab)
                elif leaf == 2:
                    tab = [valeur, Noeud(noeudPrecedent, attribut, 1, 0)]
                    noeudPrecedent.tabShield.append(tab)

        else:
            for j in range(0, length):
                leaf = isLeaf(s, i)
                if leaf == 0:
                    tab = [valeur, Noeud(noeudPrecedent, attribut, 0, 0)]
                    noeudPrecedent.tabShield.append(tab)
                    calculNode(s, i)
                elif leaf == 1:
                    tab = [valeur, Noeud(noeudPrecedent, attribut, 1, 1)]
                    noeudPrecedent.tabShield.append(tab)
                elif leaf == 2:
                    tab = [valeur, Noeud(noeudPrecedent, attribut, 1, 0)]
                    noeudPrecedent.tabShield.append(tab)

