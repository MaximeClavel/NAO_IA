# coding: utf-8

class Noeud:

    def __init__(self, attribut):
        self.attribut = attribut
        self.children = []
        self.isLeaf = 0
        self.resultat = -1
        #print 'Noeud ' + self.attribut + ' créé'

    def testCarte(self, carte):
        value = carte.getValueForAttribute(self.attribut)
        print 'Test en cours dans le noeud : ' + self.attribut + ' isLeaf : ' + str(self.isLeaf) + ' resultat => ' + str(self.resultat)

        if self.isLeaf == 1:
            carte.poids = self.resultat
            print ''

        for elem in self.children:
            #print 'Attr : ' + self.attribut + ' Valeur : ' + value + ' Element : ' + str(elem[0])
            if int(value) == elem[0]:
                elem[1].testCarte(carte)
        
        print ''

    def isTerminal(self, tabVrai, tabFaux):
        print 'Debut isTerminal --- isLeaf => ' + str(self.isLeaf) + ' --- resultat => ' + str(self.resultat)
        if len(tabVrai) > 0 and len(tabFaux) > 0:
            return 0
        elif len(tabVrai) > 0 and len(tabFaux) == 0:
            #self.isLeaf = 1
            #self.resultat = 1
            print 'Feuille Créée pour l\'attribut : ' + self.attribut + ' avec pour résultat : Oui'
            return 1
        elif len(tabVrai) == 0 and len(tabFaux) > 0:
            #self.isLeaf = 1
            #self.resultat = 0
            #print 'Fin isTerminal --- isLeaf => ' + str(self.isLeaf) + ' --- resultat => ' + str(self.resultat)
            print 'Feuille Créée pour l\'attribut : ' + self.attribut + ' avec pour résultat : Non'
            return 1
