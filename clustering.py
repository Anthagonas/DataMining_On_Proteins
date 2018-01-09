# -*- coding : utf-8 -*-
"""
DataMining program : read 3 JSon files
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
from json import load
from GetDataCriteria import *

#main script for clustering
initialDic = getCriterias(loadFiles(), ["seq",'seq_length',"fasta"])
#initialDic = {"accession number" : ["criteria1" : value,"crit2":value,...]}
#TODO : for keys,val in initialDic  find val[i] with crit=searched crit and cluster
