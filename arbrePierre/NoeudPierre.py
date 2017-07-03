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
        print 'Test en cours dans le noeud : ' + self.attribut

        if self.isLeaf == 1:
            carte.poids = self.resultat

        for elem in self.children:
            if value == elem[0]:
                elem[1].testCarte(carte)

    def isTerminal(self, tabVrai, tabFaux):
        if len(tabVrai) > 0 and len(tabFaux) > 0:
            return 0
        elif len(tabVrai) > 0 and len(tabFaux) == 0:
            self.isLeaf = 1
            self.resultat = 1
            print 'Feuille Créée pour l\'attribut : ' + self.attribut + ' avec pour résultat : Oui'
            return 1
        elif len(tabVrai) == 0 and len(tabFaux) > 0:
            self.isLeaf = 1
            self.resultat = 0
            print 'Feuille Créée pour l\'attribut : ' + self.attribut + ' avec pour résultat : Non'
            return 1
