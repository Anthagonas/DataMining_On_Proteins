getwd()
setwd("D:/Program Files (x86)/GitProject/DataMining_On_Proteins/")
#install.packages("ggplot2")
#install.packages("ggdendro")
library("cluster")
library("ggplot2")
library("ggdendro")
#Loading the csv with all protein needed values
# change row names to "entry_name" ?
data<-read.csv("clusters.csv",sep=",",row.names = 2)
data<-subset(data,select = -seq)
data<-subset(data,select = -name)
data_diana<-diana(data,FALSE)
data_diana
dg <- as.dendrogram(data_diana)
ddata <- dendro_data(data_diana)
ggplot() + 
  geom_segment(data = ddata$segments, 
               aes(x = x, y = y, xend = xend, yend = yend))


data_agnes<-agnes(data,FALSE)
data_agnes
dg <- as.dendrogram(data_agnes)
ddata <- dendro_data(data_agnes)
ggplot() + 
  geom_segment(data = ddata$segments, 
               aes(x = x, y = y, xend = xend, yend = yend))
