# coding: utf-8

from math import *

class Arbre:

    def __init__(self, exemples):
        self.exemples = exemples
        # [Valeur, Attribut, Parite, Tete, Couleur, Bonne carte]
        # Huit de carreau qui est passe [8, 1, 1, 0, 0, 1]
        # Roi de trèfle qui ne passe pas [13, 0, 0, 1, 0, 0]


    ## FONCTION ENTROPIE ##
    def calculEntropie(self, pOui, pNon):
        nbTotal = pOui + pNon
        return (-pOui/nbTotal) * log(pOui/nbTotal, 2) - (pNon/nbTotal) * log(pNon/nbTotal, 2)


    ## FONCTION PERTINENCE ##
    def calculPertinance(self, attribut):
    	arr1 = calculP(attribut, 0);
        arr2 = calculP(attribut, 1);
        if attribut == "ciel" or attribut == "temperature" :
            double[] arr3 = calculP(attribut, 2);
            return this.EntropieColonne - arr1[0]/this.nbElem * calculEntropie(arr1) - arr2[0]/this.nbElem * calculEntropie(arr2) - arr3[0]/this.nbElem *calculEntropie(arr3);
        
        else 
            return this.EntropieColonne - arr1[0]/this.nbElem * calculEntropie(arr1) - arr2[0]/this.nbElem * calculEntropie(arr2);
    




    ##
    def calculP(self, attribut, valeur):

    	double pOui = 0.0; 
        double pNon = 0.0;
        switch(attribut) {
            case "ciel":
                for(Jour j : list) {
                    if (j.getCiel() == valeur && (j.getAttribute(currentNode) == currentNodeValue || currentNode == "root")) {
                        if (j.getJouer() == true) {
                            pOui++;
                        } else {
                            pNon++;
                        }
                    }
                }
                break;
            case "temperature":
                for(Jour j : list) {
                    if (j.getTemperature() == valeur && (j.getAttribute(currentNode) == currentNodeValue || currentNode == "root")) {
                        if (j.getJouer() == true) {
                            pOui++;
                        } else {
                            pNon++;
                        }
                    }
                }
                break;
            case "humidite":
                for(Jour j : list) {
                    if (j.getHumidite() == valeur && (j.getAttribute(currentNode) == currentNodeValue || currentNode == "root")) {
                        if (j.getJouer() == true) {
                            pOui++;
                        } else {
                            pNon++;
                        }
                    }
                }
                break;
            case "vent":
                for(Jour j : list) {
                    if (j.getVent() == valeur && (j.getAttribute(currentNode) == currentNodeValue || currentNode == "root")) {
                        if (j.getJouer() == true) {
                            pOui++;
                        } else {
                            pNon++;
                        }
                    }
                }
                break;
            default:
                break;
        }
        double[] array = {pOui, pNon};
        return array;