setwd("/net/cremi/amlaport/espaces/travail/M2_bioinfo/DEA/DataMining_On_Proteins/")
library(ggplot2)
#Loading the csv with all protein needed values
data<-read.csv("clusters.csv",sep=",")
#displaying histogram of the desired criteria (change the data$ value to display other histograms)
ggplot(as.data.frame(data$seq_length), aes(x=factor(data$seq_length))) + 
  geom_bar(fill="lightgreen", color="grey50") + 
  scale_x_discrete(breaks=seq(0,35000,by=250))
