library(dplyr)
library(datasets)
library(ggplot2)
library(caret)
library(tidyr)
library(stringr)
library(corrgram)
library(Hmisc)

train_data <- read.csv("train.csv", na.strings = "")
test_data <- read.csv("test.csv", na.strings="")

#Create column Survived on Test Data and fill it with NA due to no information 
test_data$Survived <- NA

#combine train data and test data then split out
rest_raw <- rbind(train_data,test_data)
#print(dim(rest_raw))
#1309 row and 12 columns

#Changing "Name" and "Ticket" variable to character 
rest_raw$Ticket <- as.character(rest_raw$Ticket)
rest_raw$Name <- as.character(rest_raw$Name)
#print(names(rest_raw))

#throw out the PassengerID column in rest_raw
res <- rest_raw[,-1] #which is first column
#print(summary(res))

#watching NA value in the newest data
#print(summary(is.na(res)))
#conclusion:
# 1. Age has 263 values is NA (need to deal with this because Age is important)
# 2. Survived has 418 values is NA (because combine test and train data so this value can be acceptable)
# 3. Embarked has 2 values is NA which can acceptable as well
# 4. Fare has 1 value is NA
# 5. Cabin contains 1014 values is NA - might need to drop if nescessary 

# Dealing with missing value
# 1. Embarked
#print(table(res$Embarked))
#replace with character "S"
res$Embarked[is.na(res$Embarked)] <- "S"
#check the work
which(is.na(res$Embarked))

# 2. Fare 
# Imputed the mean 

res$Fare[is.na(res$Embarked)] <- with(res,ave(Fare,Pclass, FUN = function(x) median(x,na.rm = TRUE)))[is.na(res$Fare)]
#check the work
which(is.na(res$Embarked))

#create title column base on Name column 
res$Title <- NA
res$Title <- str_sub(res$Name, str_locate(res$Name,",")[,1] + 2, str_locate(res$Name,"\\.")[,1]-1)
#print(summary(res))
#turn in to factor level 18
res$Title <- factor(res$Title)


#Create LastName base on Title and Name
res$LastName <- NA
reg.ex1 <- ".*,"
res$LastName <- str_extract(res$Name,reg.ex1)
res$LastName <- gsub(",","",res$LastName)
#print(head(table(res$LastName)))

#Create 2 new column name TkPre and TkNum base on the first character on Ticket and the last character
res$TkPre <- NA 
res$TkNum <- NA

#Deal with TkPre
reg.ex2 <- ".*\\s|^[A-Z].*(?![0-9])$"
res$TkPre <- str_extract(res$Ticket,reg.ex2)
res$TkPre <- gsub("\\.|\\s|/", "",res$TkPre)
res$TkPre[is.na(res$TkPre)] <- "_"
res$TkPre <- factor(res$TkPre)

#print(summary(res$TkPre))

#Deal with TkNum
reg.ex3 <- "\\s[0-9]{1,}|^(?![A-Z]).*"
res$TkNum <- str_extract(res$Ticket,reg.ex3)
#Not using Gsub due to the character is numeric
res$TkNum[is.na(res$TkNum)] <- "0" #replace with 0 at NaN will not affect much to the data
res$TkNum <- as.numeric(res$TkNum)

#Create 2 new columns - Family Size and Rel Family Size
# 1. Family Size is to classify the number of people in SibSp and Parch
# 2. Use that data to classify small large or self
res$FamilySize <- res$SibSp + res$Parch + 1
res$relFamilySize <- NA
res$relFamilySize <- ifelse(res$FamilySize == 1, "self", 
                            ifelse(res$FamilySize <= 4, "small", "large")) 
res$relFamilySize <- factor(res$relFamilySize)
#print(table(res$relFamilySize))

#convert survived to int
res$Survived <- as.integer(res$Survived)

#Return the Age missing value - deal with it
#print(table(is.na(res$Age))) #contain 263 values is missing

#create a heatmap to reveal the relationship of each columns
#corrgram(res)
#print(rcorr(res$Age,res$Pclass))

familyAgg <- res %>% group_by(LastName) %>% summarise(n=sum(Survived, na.rm=TRUE))
familyDf <- data.frame(familyAgg)
rownames(familyDf) <- familyDf[,1]
res$FamilySurvived <- NA 

for(i in 1:length(res$LastName)){
  surname <- res$LastName[i]
  res$FamilySurvived[i] <- familyDf[surname,2] 
}

#Create Prop Survived Column
res$PropSurvived <- res$FamilySurvived/res$FamilySize

#Create SibSp Live column
res$SibSpLive <- ifelse(res$FamilySurvived>0 & res$SibSp!= 0, T, F)

#Create Parch Live column
res$ParchLive <- ifelse(res$FamilySurvived>0 & res$Parch!=0, T, F)

#Fill in the NaN position in Age part -
res$Age[is.na(res$Age)] <- with(res, ave(Age, Pclass, Title,FUN = function(x) median(x, na.rm=TRUE)))[is.na(res$Age)]

#Checking if there is any missing data
#print(which(is.na(res$Age)))
#row 980 is still missing => deal with it
require(dplyr)
tbl <- res %>% group_by(Pclass) %>% summarise(median(Age, na.rm=TRUE))
res$Age[980] <- tbl[3,2]
## Convert to numeric
res$Age <- as.numeric(res$Age)

#Create a relAge column to
res$relAge <- NA
res$relAge <- ifelse(res$Age < 7, "young child",ifelse(res$Age < 18, "child", ifelse(res$Age < 41, "young_adult", "adult")))
#Convert to factor
res$relAge <- factor(res$relAge)

#Create a CabinL 
res$CabinL <- NA
res$CabinL <- factor(substr(res$Cabin, start=1, stop=1))

res$CabinFloor <- NA
res$CabinFloor <- ifelse(res$CabinL=="A", 1, 
                         ifelse(res$CabinL=="B", 2, 
                                ifelse(res$CabinL=="C", 3, 
                                       ifelse(res$CabinL=="D", 4, 
                                              ifelse(res$CabinL=="E", 5,
                                                     ifelse(res$CabinL=="F", 6, 
                                                            ifelse(res$CabinL=="G", 7, 
                                                                   ifelse(res$CabinL=="T", 0, NA))))))))
res$CabinFloor <- as.integer(res$CabinFloor)

res$CabinFloor[is.na(res$CabinFloor)] <- with(res, ave(CabinFloor, Pclass,
                                                       FUN = function(x) mean(x, na.rm=TRUE)))[is.na(res$CabinFloor)]

res$relCabinFloor <- NA
res$relCabinFloor <- ifelse(res$CabinFloor < 4, "upper half", "lower half")
res$relCabinFloor <- factor(res$relCabinFloor)

## Remove Name (3), Ticket (8), Cabin (10), LastName (13), FamilySurvived (18), 
## PropSurvived (19), CabinL (24), CabinFloor (25)
train <- res[1:891, c(-3, -8, -10, -13, -18, -19, -24, -25)] 
test <- res[892:1309, c(-3, -8, -10, -13, -18, -19, -24, -25)] 

library(randomForest)
set.seed(0)
rf <- randomForest(factor(Survived)~ Pclass+Sex+Age+SibSp+Parch+Fare+Title+ 
                     ParchLive+SibSpLive+TkPre+TkNum+  
                     FamilySize+relFamilySize, data=train, ntree=401)
importance(rf)

out.rf <- predict(rf, newdata=test)
mean(out.rf == test_data$Survived)

test$Survived <- out.rf 
