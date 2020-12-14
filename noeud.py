#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codage as c
# Liste contenant tous les noeuds qui contiennent au moins une feuille
listeFeuilles = []

# Fonction qui retourne la liste de feuilles
def getFeuilles():
        return listeFeuilles

class Noeud:
    # Initialisation du noeud
    def __init__(self):
        self.gauche = None
        self.droite = None
        self.frequence = None
        self.parent = None

    def __str__(self):
        return "La fréquence du noeud est de : " + str(self.frequence)

    # Ajout de la fréquence du noeud
    def setFrequence(self):
        self.frequence= c.getFrequence(self.gauche) + c.getFrequence(self.droite)
    
    # Ajouter un parent au noeud (le parent est donc un noeud également)
    def setParent(self, noeud):
        self.parent = noeud

    # Fonction qui affecte les fils au noeud et ajoute 
    def createNoeud(self, elt1, elt2):
        self.gauche = elt1
        self.droite = elt2
        # On affecte le noeud parent si le fils est un noeud
        if type(elt1) is Noeud:
            elt1.setParent(self)
        if type(elt2) is Noeud:
            elt2.setParent(self)
        # Ajouter la fréquence du noeud
        self.setFrequence()
        # Si le noeud contient au moins une feuille, on l'ajoute à la liste des feuilles
        if type(elt1) is not Noeud or type(elt2) is not Noeud:
            listeFeuilles.append(self)

