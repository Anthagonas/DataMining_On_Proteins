# -*- coding: utf-8 -*-
"""
DataMining program : read 3 JSon files
gather proteins' criteria values
Json format :
{ key1 :
    {key2:,key3:,key4:,key5:,key6:,key7 :
        [{key8:,key9 : [],key10:,key11:,key12:,key13:}]
    }
}
key7 correspond to the domains (key name is "fasta")
Key names may vary
"""
#Script de Data-Mining sur un ensemble de protéines de differentes espèces
#Py3
from json import load


def recup_data(dic, crit):
    """
    returns the value of a given key within a python dictionnary
    """
    #TODO : being able to process domains ( key name = "fasta")
    return dic[crit]

def getCriterias(FileList, criteriaList):
    """
    processes the DataBase (FileList)
    gathers the values of the criteria of interest
    """
    #TODO : trouver/creer algo de clustering
    file_count = 0
    entry_count = 0
    clusterList = {}
    for files in FileList:
        file_count += 1
        print("\nCalcul sur le fichier {}...\n".format(file_count))
        """"
        gathering the considered criteria from all proteines and their name
        """
        for proteinName, proteinDicValues in files.items():
            entry_count += 1
            clusterList[proteinName] = {critere : recup_data(proteinDicValues, critere)}
    print("{} lignes récupérées... Preparation au clustering...\n".format(entry_count))
    return clusterList


if __name__ == '__main__':
    #execute script
    clusterList = {} # Protein name : value
    file_count = 0
    entry_count = 0
    print("Nom du critere de clusterisation\n")
    critere = input()
    print("Nom du premier fichier (sans l'extension .json) :\n")
    file1 = open(input()+".json")
    print("\nNom du deuxième fichier (sans l'extension .json) :\n")
    file2 = open(input()+".json")
    print("\nNom du dernier fichier (sans l'extension .json) :\n")
    file3 = open(input()+".json")

    print("Chargement des fichiers...\n")
    json1 = load(file1)
    json2 = load(file2)
    json3 = load(file3)
    print("Fichiers correctement chargés !\n")

    print(getCriterias([json1, json2, json3], ["seq"]))
