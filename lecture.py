#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Fonction pour lire le fichier
def rd(fichier):
    filin = open("./texteEncode.txt", "r")
    lec = filin.readlines()
    filin.close()
    return lec