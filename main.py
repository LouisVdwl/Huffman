#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codage as c
import lecture as l
import noeud as n
import decodage as d

# Driver Code 
if __name__ == '__main__': 
    arbre = c.build_Huffman_Tree(c.build_Frequency_table(l.rd("./texteEncode.txt")[0]))
    print(d.decodage(arbre, c.code_text(l.rd("./texteEncode.txt")[0]))[::-1])
    print(c.code_text(l.rd("./texteEncode.txt")[0]))