# -*- coding: utf-8 -*-
#Script de Data-Mining sur un ensemble de protéines de differentes espèces
#Py3
from json import load;


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
clusterResults = {};
print ("Nom du critere de clusterisation\n");
critere = input();
print ("Nom du premier fichier (sans l'extension .json) :\n");
file1 = open(input()+".json");
print ("\nNom du deuxième fichier (sans l'extension .json) :\n");
file2 = open(input()+".json");
print ("\nNom du dernier fichier (sans l'extension .json) :\n");
file3 = open(input()+".json");
print ("Chargement en cours...\n");
for item in file1 :
    """
    gathering the considered criteria from all proteines and their name
    """
    clusterList[item["name"]]=recup_data(item,critere);
for keys,values in clusterList :
    if not keys in clusterResults :
        clusterResults[keys] =1;
    else :
        clusterResults[keys] +=1;

print(clusterResults);
