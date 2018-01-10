# -*- coding : utf-8 -*-
"""
DataMining program : read JSon files
gather proteins' criteria values
and creates clusters
Json format :
{ key1 :
    {key2:,key3:,key4:,key5:,key6:,key7 :
        [{key8:,key9 : [],key10:,key11:,key12:,key13:}]
    }
}
key7 correspond to the domains (key name is "fasta")
Key names may vary
"""
from GetDataCriteria import *
from math import sqrt

def analyzeCluster(dic,crit,finalList):
    return


#main script for clustering
clusteredList=[]
critList=["seq",'seq_length',"fasta","protein_existence"]
initialDic = getCriterias(loadFiles(), critList)
print(initialDic)
histogrammes={}
valuelist=[]
#initialDic = {"accession number" : {"criteria1" : value,"crit2":value,...}, "accesN°2" : {}}
for crit in critList:
    for prot,subDic in initialDic.items():
        valuelist.append(subDic[crit])
        analyzeCluster(initialDic, crit, clusteredList)  