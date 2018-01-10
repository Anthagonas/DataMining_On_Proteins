# -*- coding : utf-8 -*-
"""
DataMining program : read JSon files
gather proteins' criteria values
and processes histograms counts
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

def countEachValue(list):
    valueDic={}
    for item in list:
        if not item in valueDic :
            valueDic[item] =1
        else :
            valueDic[item] +=1
    return valueDic

#main script for histograms
critList=['seq_length',"fasta","protein_existence","protein_existence"]
initialDic = getCriterias(loadFiles(), critList)
histogrammes={} #contain for each criteria the repatition of the values
valueList=[]
for crit in critList:
    for prot,subDic in initialDic.items():
        valueList.append(subDic[crit])
    histogrammes[crit]=valueList
    valueList=[]
for key,value in histogrammes.items():
    histogrammes[key]=countEachValue(histogrammes[key])
print(histogrammes)