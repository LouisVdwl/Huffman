#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import json
import noeud as n

# Création de la table des fréquences
def build_Frequency_table(txt):
    tableFrequence = []
    for ltr in enumerate(txt):
        if ltr[1] not in [element[0] for element in tableFrequence]:
            tableFrequence.append([ltr[1], nombreOccurence(txt, ltr[1])])
    return sorted(tableFrequence, key=lambda frq: frq[1])

# Calcul du nombre d'occurence de chaque lettre dans le txt
def nombreOccurence(txt,ltr):
    i = 0
    for elt in txt:
        if ltr == elt:
            i +=1
    return i

# Retour de la fréquence de l'element passé en params
def getFrequence(element):
        ret = lambda f:type(f) is n.Noeud and f.frequence or f[1] 
        return ret(element)

# Création de l'arbre de Huffman à partir de la table de fréquence
def build_Huffman_Tree(tableFrequence):
    arbre = list(tableFrequence)
    print(arbre)
    # Tant que la liste ne contient pas qu'un seul noeud
    while len(arbre) != 1:
        # Création du premier noeud avec les deux premières valeurs de la table de fréquences
        newNoeud = n.Noeud()
        newNoeud.createNoeud(arbre[0], arbre[1])
        # Suppression des elements utilisés pour faire la liste
        del arbre[0:2]
        # Ajout du noeud dans la liste de l'arbre
        insertNoeudByFrequence(newNoeud, arbre)
        print(arbre)
    return arbre

# Fonction qui ajoute un noeud dans la liste arbre en respectant la fréquence des elements
def insertNoeudByFrequence(noeud, liste):
    # Si ce n'est pas le dernier noeud de l'arbre
    if(len(liste) != 0):
        if getFrequence(noeud) >= getFrequence(liste[-1]):
            liste.append(noeud)
        else:
            for i in range(len(liste)):
                # Fréquence de l'élement dans la liste
                freq = getFrequence(liste[i])
                # Si la fréquence du noeud est < à la fréquence de l'element, on ajoute le noeud avant cet element
                if getFrequence(noeud) < freq :
                    liste.insert(i, noeud)
                    break
    else:
        liste.append(noeud)

# Retourne une liste a deux dimensions contenant la lettre ainsi que son code binaire
def get_Dict_Huffman(carac):
    # Recuperation de la liste des feuilles
    feuilles = n.getFeuilles()
    # Initialisation du code du caractère
    code = ""
    # Recherche du noeud qui contient la bonne feuille
    for elt in feuilles:
        # Si le fils gauche est la bonne lettre
        if type(elt.gauche) is not n.Noeud and elt.gauche[0] == carac:
            # Affecte le noeud à nd
            nd = elt
            # Le code de la lettre commence donc par 0 car c'est le fils gauche
            code += str(0)
        elif type(elt.droite) is not n.Noeud and elt.droite[0] == carac:
            nd = elt
            code += str(1)
    # Tant que le noeud courant n'est pas le dernier noeud (celui qui représente l'arbre)
    while nd.parent != None:
        # On regarde si le noeud courant est à gauche ou à droite
        if nd.parent.gauche is nd:
            code += str(0)
        else:
            code += str(1)
        nd = nd.parent

        
    # On ajoute la lettre avec le code dans la liste 
    return [carac, code[::-1]]

# Retourne le texte passé en paramètre sous forme binaire
def code_text(txt):
    sortie = ""
    # Pour chaque carac présent dans le texte on concatene son code avec la variable de retour
    for ltr in txt:
        sortie += get_Dict_Huffman(ltr)[1][::-1]
    return sortie[::-1]