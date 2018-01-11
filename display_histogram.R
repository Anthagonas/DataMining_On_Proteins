setwd("D:/Program Files (x86)/GitProject/DataMining_On_Proteins/")
#Loading the csv with all protein needed values
data<-read.csv("clusters.csv",sep=",")
#displaying histogram of the desired criteria (change the data$ value to display other histograms)
hist(as.numeric(data$seq_length), main="histogram of the sequences length",xlab="sequence length (AA)")
