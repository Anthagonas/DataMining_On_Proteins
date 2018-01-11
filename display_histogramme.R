setwd("D:/Program Files (x86)/GitProject/DataMining_On_Proteins/")
test<-read.csv("clusters.csv",sep=",")

hist(as.numeric(test$protein_existence))
