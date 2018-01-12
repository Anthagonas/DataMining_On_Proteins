# coding: utf-8
"""
DataMining program : read JSon files
gather proteins' criteria values
and processes the percentage of present value
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

###
#MAIN script
###
"""
Loading the .json files
"""
print("Nom du premier fichier (sans l'extension .json) :\n")
file1 = open(input()+".json")
print("\nNom du deuxième fichier (sans l'extension .json) :\n")
file2 = open(input()+".json")
print("\nNom du dernier fichier (sans l'extension .json) :\n")
file3 = open(input()+".json")
print("Chargement en cours...\n")

json1 = load(file1)
json2 = load(file2)
json3 = load(file3)

"""
Initializing the counts and dictionaries
"""
entry_count = 0
fasta_count = 0
file_count = 0
entry_dic = {}
fasta_dic = {}

"""
For each accession number (= protein, also key1 in the structure)
checks the value bound to the key, if there is a value, adds 1 to the count.
For the domains ( key7="fasta" ), same method for each key stored within the "fasta" key.
The result here is a sum of the non-empty keys (same for the keys within fasta key)
"""
for file in (json1, json2, json3):
	file_count += 1
	print("\nCalcul sur le fichier {}...\n".format(file_count))
	for masterkey,subdic in file.items() :
		entry_count += 1
		for key,value in subdic.items() :
			if str(value).lower() not in ["",None,"none",[],[""],"."] :
				if value :
					if not key in entry_dic :
						entry_dic[key] =1
					else :
						entry_dic[key] +=1
			if key == "fasta" :
				for strand_dic in value :
					fasta_count += 1
					for fastakey,fastavalue in strand_dic.items() :
						if str(fastavalue).lower() not in ["",None,"none",[],[""],"."] :
							if fastavalue :
								if not fastakey in fasta_dic :
									fasta_dic[fastakey] =1
								else :
									fasta_dic[fastakey] +=1

print("{} lignes récupérées... calcul des pourcentages...\n".format(entry_count))

"""
Processing the percentages of actual values.
For the main criteria : dividing the non-empty count by the protein count
For the domains ( ="fasta") : dividing the non-empty count by the total fasta count.
"""
for entries,value in entry_dic.items() :
	entry_dic[entries] /= (entry_count/100.0)
for entries,value in fasta_dic.items() :
	fasta_dic[entries] /= (fasta_count/100.0)

"""
Displaying percentages.
"""
print("Résumé des pourcentages :\n")
print(entry_dic,"\n")
print("Precision des pourcentages pour l'entrée : 'fasta'\n")
print(fasta_dic,"\n")
print("enregistrement des valeurs dans le fichier : 'percentages.txt'")

"""
Writting the results in a .txt file.
NB : percentages might be rounded in the output file.
"""
with open("percentages.txt", 'w') as out:
	for entries,value in entry_dic.items() :
		out.write(str(entries) + ' : ' + str(value)+ '%\n')
	out.write("valeurs pour 'fasta' :\n")
	for entries,value in fasta_dic.items() :
		out.write(str(entries) + ' : ' + str(value)+ '%\n')
