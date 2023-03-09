library(tidyr)
library(dplyr)

#Reads in sample data for bacteria hits of each sample and IBS vs Healthy
microData <- read.delim("~/Desktop/CaSB185/CASB M185 Data1.txt", header=TRUE)
microMeans <- read.delim("~/Desktop/CaSB185/CASB M185 Data2.txt", header=TRUE)

#Cleans up datasets to prepare for filtering and analysis
microData <- microData[,c(1:2)]
microMeans <- microMeans[,c(1:7)]
microMeans = microMeans%>%fill(Sample..)

#Calculate the mean value for each of the bacteria for each sample
test = microMeans %>% group_by(Sample..) %>% summarise(Bifidobacterium = mean(Bifidobacterium), 
                                                       Prevotella = mean(Prevotella), 
                                                       Lachnospira = mean(Lachnospira),
                                                       Eubacterium = mean(Eubacterium),
                                                       Lactobacillus = mean(Lactobacillus))

#Removes the sample # column to prepare for combination with other dataset
test <- test[,c(2:6)]

#Combines the microData and test datasets into a single dataset
microSorted <- cbind(microData, test)

#Subset the dataset into two separate datasets for IBS and Healthy samples
IBS <- microSorted[microSorted$IBS.Control == "IBS",]
Healthy <- microSorted[microSorted$IBS.Control == "Healthy",]

#Running T-tests for each bacteria
t.test(IBS$Bifidobacterium, Healthy$Bifidobacterium, var.equal = TRUE, alternative = "two.sided", conf.level = 0.95)
t.test(IBS$Prevotella, Healthy$Prevotella, var.equal = TRUE, alternative = "two.sided", conf.level = 0.95)
t.test(IBS$Lachnospira, Healthy$Lachnospira, var.equal = TRUE, alternative = "two.sided", conf.level = 0.95)
t.test(IBS$Lactobacillus, Healthy$Lactobacillus, var.equal = TRUE, alternative = "two.sided", conf.level = 0.95)
t.test(IBS$Eubacterium, Healthy$Eubacterium, var.equal = TRUE, alternative = "two.sided", conf.level = 0.95)
