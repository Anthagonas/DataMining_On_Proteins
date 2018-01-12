setwd("/Your/Path/To/The/CSV/File")
install.package("ggplot2")
library(ggplot2)

#Loading the csv with considered protein values
data<-read.csv("clusters.csv",sep=",")

#CREATING AN HISTOGRAM :
#The following plot display the histogram for a single column in the CSV.

#1. In order to change the column displayed, change the two following "data$XXXXXX" by "data$ColumnNameYouWant"
#example : ggplot(as.data.frame(data$phi), aes(x=factor(data$phi)))  to display the phi histogram

#2. you can change the histogram colors using the fill= and color= from the "geom_bar()" method.

#NOTE : you might want to change the scaling of the histogram, check the "scale_x_discrete" values below.
ggplot(as.data.frame(data$seq_length), aes(x=factor(data$seq_length))) + 
  geom_bar(fill="lightgreen", color="grey50") + 
  scale_x_discrete(breaks=seq(0,35000,by=250)) #breaks=seq(xmin,xmax,by=step)
