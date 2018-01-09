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
import GetDataCriteria
