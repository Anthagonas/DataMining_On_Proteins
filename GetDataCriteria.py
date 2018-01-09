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

def loadFiles(fileCount=3):
    fileList = []
    jsonList = []
    for i in range(1,fileCount):
        print("Nom du fichier N°{}(sans l'extension .json) :\n".format(i))
        fileList.add(open(input()+".json",r))

    print("Chargement des fichiers...\n")
    for i in range(len(fileList)):
        print("Chargement du fichier N°{}...\n".format(i+1))
        jsonList.add(load(fileList[i]))
        print("Fichier correctement chargé !\n")
    return jsonList

def recup_data(dic, crit):
    """
    returns the value of a given key within a python dictionnary
    """
    if crit == "fasta":
        return len(dic[crit])
    return dic[crit]

def getCriterias(FileList, criteriaList):
    """
    processes the DataBase (FileList)
    gathers the values of the criteria of interest
    FileList = loaded json files
    criteriaList = list of string containing keys to gather
    """
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
            for critere in criteriaList:
                if not proteinName in clusterList :
                    clusterList[proteinName] = [{critere : recup_data(proteinDicValues, critere)}]
                else :
                    clusterList[proteinName].add({critere : recup_data(proteinDicValues, critere)})
    print("{} lignes récupérées... Preparation au clustering...\n".format(entry_count))
    return clusterList


if __name__ == '__main__':
    #execute script
    print("Nom du critere de clusterisation\n")
    critere = input()
    fileList=loadFiles();

    print(getCriterias(fileList, [critere]))
