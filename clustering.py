item# -*- coding: utf8 -*-
#Script de Data-Mining sur un ensemble de protéines de differentes espèces
#Py3


def recup_data(dic,crit):
    """
    fetches in a python dictionnary if the key exists and returns the value bond to it
    else returns "N/A"
    """
    for tag in dic.keys():
        if tag.equals(crit) :
            return dic[tag];
    return "N/A"



#parcourir la BD
#recup les datas d'interet
#en fonction du critere choisir, regrouper les protéines
#TODO : trouver/creer algo de clustering
clusterList = {};
critere = "";
for item in file_x :
    """
    gathering the considered criteria from all proteines and their name
    """
    clusterList[item["name"]]=recup_data(item,critere);
