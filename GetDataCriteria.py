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
import ph_table

def loadFiles(fileCount=3):
    fileList = []
    jsonList = []
    for i in range(0,fileCount):
        print("Nom du fichier N°{}(sans l'extension .json) :\n".format(i+1))
        fileList.append(open(input()+".json"))

    print("Chargement des fichiers...\n")
    for i in range(len(fileList)):
        print("Chargement du fichier N°{}...\n".format(i+1))
        jsonList.append(load(fileList[i]))
        print("Fichier correctement chargé !\n")
    return jsonList

def getPhiValue(seq):
    phi_value = 0.0
    count = 0
    for letter in seq:
        if letter == "X":
            continue
        count += 1
        phi_value +=ph_table.PHTABLE[letter]
    return round(phi_value/len(seq), 2)


def recup_data(dic, crit):
    """
    returns the value of a given key within a python dictionnary
    """
    if crit=="fasta":
        try:
            return len(dic[crit])
        except KeyError :
            return 0
    if crit=="phi":
        return getPhiValue(dic["seq"])
    
    return dic[crit]

def getCriterias(fileList, criteriaList):
    """
    processes the DataBase (FileList)
    gathers the values of the criteria of interest
    FileList = loaded json files
    criteriaList = list of string containing keys to gather
    """
    file_count = 0
    entry_count = 0
    clusterList = {}
    for files in fileList:
        file_count += 1
        print("\nCalcul sur le fichier {}...\n".format(file_count))
        """"
        gathering the considered criteria from all proteines and their name
        """
        for proteinName, proteinDicValues in files.items():
            entry_count += 1
            for critere in criteriaList:
                if proteinName in clusterList :
                    clusterList[proteinName][critere] = recup_data(proteinDicValues, critere)
                else:
                    clusterList[proteinName]={}
                    clusterList[proteinName][critere] = recup_data(proteinDicValues, critere)
                if critere == "seq":
                    clusterList[proteinName]["phi"] = recup_data(proteinDicValues, "phi")



    print("{} lignes récupérées... Preparation au clustering...\n".format(entry_count))
    return clusterList


if __name__ == '__main__':
    #execute script
    print("Nom du critere de clusterisation\n")
    critere = input()
    fileList=loadFiles();

    print(getCriterias(fileList, [critere]))
