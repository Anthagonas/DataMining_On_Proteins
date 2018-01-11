setwd("/net/cremi/amlaport/espaces/travail/M2_bioinfo/DEA/DataMining_On_Proteins/")
#Loading the csv with all protein needed values
data<-read.csv("clusters.csv",sep=",")
#displaying histogram of the desired criteria (change the data$ value to display other histograms)
hist(as.numeric(data$seq_length), main="Histogram of the sequences length",xlab="length (in AA)",xlim=range(0,6000), labels = TRUE)
help(hist)
