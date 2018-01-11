getwd()
setwd("/net/cremi/amlaport/espaces/travail/M2_bioinfo/DEA/DataMining_On_Proteins/")
#install.packages("ggplot2")
#install.packages("ggdendro")
#install.packages("factoextra")
library("cluster")
library("ggplot2")
library("ggdendro")
library(factoextra)
#Loading the csv with all protein needed values
#taking a sample from the datas
data<-read.csv("clusters.csv",sep=",",row.names = 2)
data<-subset(data,select = -seq)
data<-subset(data,select = -name)
data<-data[sample(nrow(data), 3500), ]

#Top down Divisive analysis
data_diana<-diana(data,FALSE)
data_diana
dg <- as.dendrogram(data_diana)
ddata <- dendro_data(data_diana)
ggplot() + 
  geom_segment(data = ddata$segments, 
               aes(x = x, y = y, xend = xend, yend = yend))
grp <- cutree(data_diana, k = 5)
fviz_cluster(list(data = , cluster = grp))

#Bottom up Agglomerative nesting
data_agnes<-agnes(data,FALSE) 
data_agnes
dg <- as.dendrogram(data_agnes)
ddata <- dendro_data(data_agnes)
ggplot() + 
  geom_segment(data = ddata$segments, 
               aes(x = x, y = y, xend = xend, yend = yend))
