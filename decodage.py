#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codage as c
import noeud as n

# Fonction qui décode un texte codé 
def decodage(arbre, txt):
    # Noeud courant est le noeud qui représente l'arbre
    ndCourant = arbre[0]
    valeurSortie = ""
    # On parcours le code binaire
    for elt in txt:
        if elt == "0":
            if type(ndCourant.gauche) is n.Noeud:
                ndCourant = ndCourant.gauche
            else:
                valeurSortie += ndCourant.gauche[0]
                ndCourant = arbre[0]
        else:
            if type(ndCourant.droite) is n.Noeud:
                ndCourant = ndCourant.droite
            else:
                valeurSortie += ndCourant.droite[0]
                ndCourant = arbre[0]
    return valeurSortie
