from Bio.Cluster import kcluster
import numpy as np
import csv

csvfile=open("clusters.csv",'rb')
csv=csv.reader(csvfile,delimiter=',')
sequences=[]
for row in csv:
    sequences.append(row[2])
print sequences

matrix = np.asarray([np.fromstring(s, dtype=np.uint8) for s in sequences])
clusterid, error, nfound = kcluster(matrix)

print(clusterid)
