# DataMining_On_Proteins
This project's goal is to caracterize and regroup proteins using data similarity and compare this clustering to a "regular" likeness clustering made in biology.

## Overview

1. json files are considered as your data warehouse.
1. *create_csv.py* gathers data from previous json files and creates *clusters.csv*.
1. *clusters.csv* can be used either with *hierarchical_clustering.R* or *display_histogram.R* scripts to obtaint graphical results.

## How to use it :
### Gathering informations on your datas
Before getting started with the clustering step, you can have an overview of the missing datas in your data warehouse.

The *data_checking.py* script processes the percentages of present criteria in the datawarehouse, and stores it into a *percentages.txt* result file.

_**NOTE** : In our current datawarehouse, the "domains" are stored under the key "fasta" which may be confusing. The "fasta" key contains a list of all the domains for a protein._

### Getting the clusters.csv file
The first step is to gather datas from your data warehouse.

In order to do so, you can use the *create_csv.py* script to gather specified criterias within multiple files (see the *create_csv.py* file for more informations on the data warehouse structure, the way to change the number of files to load and the criterias to gather)
Using the *create_csv.py* script will generate a *clusters.csv* file.

_**NOTE** : you can use the *ble.json*, *ecoli.json* and *homo.json* as test samples for the script, or to check the structure of the json files._

### Obtaining the graphics
Once the clusters.csv file is ready ( or any csv file with similar data ), two scripts are available to create the graphics : 

* **display_histogram.R** : this script uses the csv file to create a **SINGLE** histogram. Check the script for more informations on how to modify the displayed histogram. This script uses the package [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html).

* **hierarchical_clustering.R** : this script uses the csv file and creates two dendrograms, first the DIANA (Divisive Analysis) dendrogram, then the AGNES (Agglomerative Nesting). Check the script for more informations on the random sample size. This script uses the package [clusters](https://cran.r-project.org/web/packages/cluster/cluster.pdf), for more information on the DIANA and AGNES analysis, and the hierarchical clustering with R, you can check [this site](http://www.sthda.com/english/wiki/print.php?id=237#agnes-and-diana-functions).

## Additionnal files
The scripts use additionnal files in order to work properly.

* **.json files** : The .json files available (homo,ecoli and ble.json) are here for the sake of simplicity, we did not use those files for our analysis, they allow fast processing through R and an easier overview of the datawarehouse structure considering their size. they can be used with *create_csv.py* and *data_checking.py*

* **GetDataCriteria.py** : This script contains the main methods to fetch values from the data warehouse. it is needed for *create_csv.py*,*data_checking.py* and *histogram_table.py* scripts.

* **ph_table.py** : This python file stores a dictionary giving the pI (Isoelectric point) of an amino acid using the 1 letter code. It is used by the *create_csv.py* script in order to process the pI value from the protein sequence.

* **histogram_table.py** : This python file processes the .json files and created a .csv file named after your criteria name. The csv file structure consist of 2 columns : the value of the criteria, and the total time this value has been found in the .json files. 
_**NOTE** : This script is depreciated since it is not usable via R, but we kept it anyway since it is possible to create an histogram via the .csv files._

* **.png files** : These are images extracted from R we used for our report, using our project's datawarehouse and scripts.
