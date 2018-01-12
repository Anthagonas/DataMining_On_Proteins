# -*- coding : utf-8 -*-
"""
DataMining program : read JSon files
gather proteins' criteria values, processes histograms counts
and writes a .txt file for each histogram
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
    """
    Counts how many times a same value appears in the list given as parameter.
    Returns a python dictionary as {value1:count, value2:count ...}.
    """
    valueDic={}
    for item in list:
        if not item in valueDic :
            valueDic[item] =1
        else :
            valueDic[item] +=1
    return valueDic

###
#main script for histograms
###
"""
The list of criteria we want the histograms from
"""
critList = ['seq_length',"fasta","protein_existence","phi"]

"""
The "final" dictionary, the one that is converted to .csv file
structure : finalDic = {"accession number" : {"criteria1" : value,"crit2":value,...}, "accesN°2" : {}}
where accession number correspond to "key1" and "criteria" to the criterias specified in the critList
see GetDataCriteria.py for more infos on getCriterias() and loadfiles()
"""
finalDic = getCriterias(loadFiles(), critList)

"""
The "output" dictionary, containing for each criteria (see critList) the histogram we want to write in a file.
see countEachValue() for more information about the histogram structures.
"""
histogrammes = {} #contain for each criteria the repatition of the values

"""
This list will contain every value for a given criteria, then will be purged before the next criteria.
"""
valueList = []
for crit in critList:
    """
    Gathering all values for a given criteria.
    """
    for prot, subDic in finalDic.items():
        valueList.append(subDic[crit])
    """
    Binding the values to the corresponding key.
    """
    histogrammes[crit] = valueList
    valueList = []
for key, value in histogrammes.items():
    """
    Processing every list of value into an histogram.
    See countEachValue for more information.
    """
    histogrammes[key] = countEachValue(histogrammes[key])

"""
Writting each histogram into a corresponding .txt file.
"""
for crit in critList:
    with open(crit+".csv", 'w') as out:
        out.write("value,count\n")
        for entries, value in sorted(histogrammes[crit].items(), key=lambda x: x[1]):
            out.write(str(entries) + ',' + str(value)+'\n')
