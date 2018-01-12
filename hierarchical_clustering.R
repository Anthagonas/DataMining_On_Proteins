getwd()
setwd("Your/path/to/the/CSV/file")

#Install the following packades if missing :
#install.packages("ggplot2")
#install.packages("ggdendro")
#install.packages("factoextra")
#install.packages("dendextend")

#Loading the packages :
library("cluster")
library("ggplot2")
library("ggdendro")
library(factoextra)
library(dendextend)


#Loading the csv with all protein needed values
#then taking a random sample from the datas
data<-read.csv("clusters.csv",sep=",",row.names = 2) #row.names is the column where your item names are stored
data<-subset(data,select = -seq) #removing some columns we don't need for the hierarchical clustering
data<-subset(data,select = -name) #same here
data<-data[sample(nrow(data), 50), ] #Taking a random sample from the table

#Top down Divisive analysis
#processing the clusters (this may take some time with huge sample size)
data_diana<-diana(data,FALSE) #FALSE option indicates that we don't have a dissamblance matrix, but a variable/observations table
#You can see the diana results by using the command : data_diana
ddata <- dendro_data(data_diana) #storing the diana result as a dendrogram data
#creating the graphical resuldisplayt
ggplot() + 
  geom_segment(data = ddata$segments, 
               aes(x = x, y = y, xend = xend, yend = yend))

#ggdendrogram displays label on the leaves, this isn't used for large samples. It is possible to use it for small datas (<= 50 seems right)
#ggdendrogram(ddata)

#Bottom up Agglomerative nesting
#processing the clusters ( this may take some time with huge sample size)
data_agnes<-agnes(data,FALSE) #FALSE option for the same reason as diana() part
#You can see the diana results by using the command : data_agnes
ddata <- dendro_data(data_agnes) #storing the diana result as a dendrogram data
#creating the graphical display 
ggplot() + 
  geom_segment(data = ddata$segments, 
               aes(x = x, y = y, xend = xend, yend = yend))

#OPTIONNAL : for small sample size
#Comparing the 2 dendrograms : shows the differences between DIANA and AGNES clustering
dgdiana <- as.dendrogram(data_diana)
dgagnes <- as.dendrogram(data_diana)
tanglegram(dgdiana, dgagnes)

