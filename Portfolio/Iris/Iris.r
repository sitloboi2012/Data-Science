library(dplyr)
library(datasets)
library(caret)
library(ggplot2)


iris <- read.csv('iris.data',header=TRUE)
colnames(iris) <- c('Sepal.Length','Sepal.Width','Petal.Length','Petal.Width','Class')
#str(iris) #150 observation and 5 columns

#split data 
#80% train and 20% test (120 observation)
sample  <- createDataPartition(iris$Class,p=0.80,list=FALSE)
#create training data
iris_train <- iris[sample,]
#str(iris_train)

#create test data (30 observation)
iris_test <-iris[-sample,]
#str(iris_test)


#summarize the Class distribution of train data
percentage <- prop.table(table(iris_train$Class)) * 100
cbind(Freq = table(iris_train$Class), Percentage = percentage)

#Visualization 
#Using 2 plots: Univariate - understand each attribute / Multivariate - understand the relationship between each attribute4

#Univariate
x <- iris_train[,1:4] #from column 1 to 4
y <- iris_train[,5] #the column 5

#boxplot
par(mfrow = c(1,4)) #create a size of window with 1 row and 4 column for 4 attribute
for (i in 1:4) {
    boxplot(x[i],main=names(iris_train)[i])
} #for each of the column will draw a boxplot with main is name of the attribute name

#bar chart
par(mfrow = c(1,3))
qplot(y, xlab='Class')

#Multivariate 
#scatter 
featurePlot(x=x,y=y,plot="ellipse",auto.key=list(columns=3))

#boxplot
featurePlot(x=x,y=y,plot="box",auto.key=list(columns=3))

#density plot
featurePlot(x=x,y=y,plot="density",scales = list(x = list(relation="free"),y = list(relation="free")), auto.key=list(column=3))


#BUILD MODEL 
#5 different model - Linear Discriminant Analysist (LDA) / Classification and Regression Tree (CART) / KNN / SVM / Random Forest

#Evaluate Algorithm
control <- trainControl(method="cv",number=10)
metric <- "Accuracy"


#Linear Discriminant Analysist (LDA)
set.seed(101)
fit.lda <- train(Class~., data=iris_train, method="lda", trControl = control, metric= metric)

#CART 
set.seed(101)
fit.cart <- train(Class~., data=iris_train, method="rpart", trControl = control, metric = metric)

#KNN
set.seed(101)
fit.knn <- train(Class~., data=iris_train, method="knn", trControl= control, metric=metric)

#SVM
set.seed(101)
fit.svm <- train(Class~., data=iris_train,method="svmRadial", trControl=control, metric = metric)

#Random Forest
set.seed(101)
fit.rf <- train(Class~., data=iris_train, method="ranger", trControl = control, metric = metric)


#result of 5 algorithm
iris.result <- resamples(list(lda = fit.lda, cart = fit.cart, knn = fit.knn, svm = fit.svm, rf = fit.rf))

print(summary(iris.result))
print(bwplot(iris.result))
print(dotplot(iris.result))


#Make predict
iris.predict <- predict(fit.lda, iris_test) #iris predict <- predict(name_model, test_data)
#confusionMatrix(iris.predict,iris_test$Class)
#If getting factor level error, change the confusionMatrix to table and the rest the same 
print(confusionMatrix(table(iris.predict, iris_test$Class)))