# coding: utf-8


class Noeud:

    def __init__(self,parent):

    	self.attribut = ''
    	self.tabShield = []
    	self.isLeaf = 0
    	self.resultat = 0
    	self.parent = parent

    def testCarte(maCarte):


    	if self.isLeaf == 1:
    		maCarte.poids = self.resultat
    		return


    	value = maCarte.getValueForAttribute(self.attribut)

    	for i in range(0,len(tabShield)):

    		if value == tabShield[i][0]:
    			tabShield[i][1].testCarte(maCarte)




