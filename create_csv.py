# -*- coding : utf-8 -*-
"""
DataMining program : read JSon files
gather proteins' criteria values
and creates a csv usable via R
Json format :
{ key1 :
    {key2:,key3:,key4:,key5:,key6:,key7 :
        [{key8:,key9 : [],key10:,key11:,key12:,key13:}]
    }
}
key7 correspond to the domains (key name is "fasta")
Key names may vary
"""
from GetDataCriteria import getCriterias, loadFiles

#main script for clustering
clusteredList = []
critList = ["entry_name","seq","seq_length","fasta","protein_existence","phi"]
initialDic = getCriterias(loadFiles(), critList)
#initialDic = {"accession number" : {"criteria1" : value,"crit2":value,...}, "accesN°2" : {}}
with open("clusters.csv", 'w') as out:
    out.write("name")
    for crit in critList:
        out.write(","+crit)
    out.write("\n")
    for entries, value in initialDic.items():
        out.write(entries)
        for crit in critList:
            out.write(","+str(value[crit]))
        out.write("\n")
