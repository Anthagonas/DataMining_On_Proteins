setwd("D:/Program Files (x86)/GitProject/DataMining_On_Proteins/")
install.packages("ggplot2")
install.packages("ggdendro")
library("cluster")
library("ggplot2")
library("ggdendro")
#Loading the csv with all protein needed values
# change row names to "entry_name" ?
data<-read.csv("clusters.csv",sep=",",row.names = 1)
data_diana<-diana(data,FALSE)
data_diana
dg <- as.dendrogram(data_diana)
ggdendrogram(dg,col=data$protein_existence)

ddata <- dendro_data(data_diana)
ggplot() + 
  geom_segment(data = ddata$segments, 
               aes(x = x, y = y, xend = xend, yend = yend,colour = data$protein_existence))

ggplot(data_diana)
plot(data_diana,col=data$protein_existence)



data_agnes<-agnes(data,FALSE)
data_agnes
plot(data_agnes)
help(plot.diana)
