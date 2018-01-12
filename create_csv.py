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
"""
critList is the list of criteria we want to fetch from the datawarehouse
it correspond to the key2-7 from our data warehouse
"""
critList = ["entry_name","seq","seq_length","fasta","protein_existence","phi"]

"""
The "final" dictionary, the one that is converted to .csv file
structure : finalDic = {"accession number" : {"criteria1" : value,"crit2":value,...}, "accesN°2" : {}}
where accession number correspond to "key1" and "criteria" to the criterias specified in the critList
see GetDataCriteria.py for more infos on getCriterias()
"""
finalDic = getCriterias(loadFiles(), critList)
with open("clusters.csv", 'w') as out:
    out.write("name")
    for crit in critList:
        out.write(","+crit)
    out.write("\n")
    for entries, value in finalDic.items():
        out.write(entries)
        for crit in critList:
            out.write(","+str(value[crit]))
        out.write("\n")
