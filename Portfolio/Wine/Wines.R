library(dplyr)
library(ggplot2)
library(caret)
library(Hmisc)

#load data
data <- read.csv("wine.data",sep=",")

#GET BASIC INFO
#print(summary(data))
print(dim(data))
#14 COLUMNS AND 178 ROWS
print(names(data))

#Check null
#print(summary(is.na(data)))
#0 null value 

#Check correlation 
res <- cor(data)
#print(round(res, 2))
#ASH COLUMNS HAS A WEAK CONNECTION WITH TYPE(Y VALUE) => MIGHT NEED TO DROP => INCREASE THE PREDICTION


#In-depth view inside data

#checking the COUNT(value) in each of the type
hist(data$type,main="Type Value Count",xlab="Type of Wine",freq = FALSE) #=> type 2 has the most value

#Split out the data (80%/20%)
sample  <- createDataPartition(data$type,p=0.80,list=FALSE)
train <- data[sample,]
test <- data[-sample]

#Create X and Y for prediction 
percentage <- prop.table(table(train$type)) * 100
cbind(Freq = table(train$type), Percentage = percentage)
x <- data[,2:13]
y <- data[,1]

library(randomForest)
set.seed(0)
rf <- randomForest(type~., data=train, ntree=401)
importance(rf)

out.rf <- predict(rf, newdata=test)
mean(out.rf == test$type)

test$type <- out.rf 

