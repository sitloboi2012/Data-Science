import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sklearn import linear_model,preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB


train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# print(train_data.head(10))

print(train_data.describe())
# 38% of people are survived is 80
# age has some missing data
# lowest age is 4 years old and the maximum age is 80

# create a table to analyze the missing data in titanic
"""train_head = train_data.head(10)
print(train_head.sort_values(ascending=False,by=["Age"]))"""
total = train_data.isnull().sum().sort_values(ascending=False)
percent1 = train_data.isnull().sum()/train_data.isnull().count()*100
percent2 = (round(percent1,1)).sort_values(ascending=False)
missing_data = pd.concat([total,percent2], axis=1, keys=["Total", "Percent"])
print(missing_data.head(5))
# Cabin got 77% of data is missing - might drop this data
# Age got 19.9% of data missing - need to evaluated - solve this problem
# Embarked got 2% of data is missing - not very important

print(train_data.columns.values)
# 11 values with 1 target (Survived)
# Feature might choose is - Age,Embarked,Sex

# create graph to see the connection between target and feature

# Survived vs Gender
survived = "survived"
not_survived = "not survived"
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,4))
plt.title("Survival base on Gender",loc="center")
woman = train_data[train_data["Sex"] == "female"]
man = train_data[train_data["Sex"] == "male"]


ax = sns.distplot(woman[woman['Survived'] == 1].Age.dropna(), bins=18, label=survived, ax=axes[0], kde=False)
ax = sns.distplot(woman[woman['Survived'] == 0].Age.dropna(), bins=40, label=not_survived, ax=axes[0], kde=False)
ax.legend()
ax.set_title("Woman")

ax = sns.distplot(man[man["Survived"] == 1].Age.dropna(), bins=18, label=survived, ax=axes[1], kde=False)
ax = sns.distplot(man[man["Survived"] == 0].Age.dropna(), bins=40, label=survived, ax=axes[1], kde=False)
ax.legend()
ax.set_title("Men")

# Embarked, Pclass vs Sex
facetGrid = sns.FacetGrid(train_data, row="Embarked", size=4.5, aspect=1.6)
facetGrid.map(sns.pointplot, "Pclass", "Survived", "Sex", palette=None, order=None, hue_order=None)
facetGrid.add_legend()

# Pclass
sns.barplot(x="Pclass",y="Survived",data=train_data)

grid = sns.FacetGrid(train_data, col="Survived", row="Pclass", size=2.2, aspect=1.6)
grid.map(plt.hist, "Age", alpha=.5, bins=20)
grid.add_legend()

# SibSp and Parch
data = [train_data,test_data]
for dataset in data:
    dataset["relatives"] = dataset["SibSp"] + dataset["Parch"]
    dataset.loc[dataset['relatives'] > 0, 'not_alone'] = 0
    dataset.loc[dataset['relatives'] == 0, 'not_alone'] = 1
    dataset['not_alone'] = dataset['not_alone'].astype(int)

print(train_data['not_alone'].value_counts())

axes = sns.factorplot('relatives',"Survived", data=train_data, aspect=2.5,)

# Preprocessing Data
train_data = train_data.drop(['PassengerId'], axis=1)

# Dealing with Missing Data

# CABIN
deck = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "U":8}
data = [train_data, test_data]

for dataset in data:
    dataset["Cabin"] = dataset["Cabin"].fillna("U0")
    dataset["Deck"] = dataset["Cabin"].map(lambda x:re.compile("([a-zA-Z]+)").search(x).group())
    dataset["Deck"] = dataset["Deck"].map(deck)
    dataset["Deck"] = dataset["Deck"].fillna(0)
    dataset["Deck"] = dataset["Deck"].astype(int)

# drop the cabin feature - not using it anymore - use the deck one
train_data = train_data.drop(["Cabin"], axis=1)
test_data = test_data.drop(["Cabin"], axis=1)

# AGE
data = [train_data,test_data]
for dataset in data:
    mean = train_data["Age"].mean()
    std = test_data["Age"].std()
    is_null = dataset["Age"].isnull().sum()

    # compute random numbers between the mean, std and is_null
    rand_age = np.random.randint(mean - std, mean + std, size=is_null)

    # fill NaN values in Age column with random values generated
    age_slice = dataset["Age"].copy()
    age_slice[np.isnan(age_slice)] = rand_age
    dataset["Age"] = age_slice
    dataset["Age"] = train_data["Age"].astype(int)

print(train_data["Age"].isnull().sum())

common_value = "S"
data = [train_data,test_data]
for dataset in data:
    dataset["Embarked"] = dataset["Embarked"].fillna(common_value)

# Coverting Features

# FARE
data = [train_data,test_data]
for dataset in data:
    dataset["Fare"] = dataset["Fare"].fillna(0)
    dataset["Fare"] = dataset["Fare"].astype(int)

# NAME
titles = {"Mr":1, "Miss":2, "Mrs":3, "Master":4, "Rare":5}
data = [train_data,test_data]
for dataset in data:
    # extract titles
    dataset["Title"] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
    # replace titles with a more common title or as Rare
    dataset["Title"] = dataset["Title"].replace(["Lady","Countess","Capt","Col","Don", "Dr", "Major", "Rev", "Sir", "Jonkheer", "Dona"], "Rare")
    dataset["Title"] = dataset["Title"].replace("Mlle","Miss")
    dataset["Title"] = dataset["Title"].replace("Ms","Miss")
    dataset["Title"] = dataset["Title"].replace("Mme","Mrs")
    # convert title to number
    dataset["Title"] = dataset["Title"].map(titles)
    # filling NaN with 0 => doesn't affect the calculation later
    dataset["Title"] = dataset["Title"].fillna(0)

# drop axis name and replace with title
train_data = train_data.drop(["Name"], axis=1)
test_data = test_data.drop(["Name"], axis=1)


# SEX - convert to numb
gender = {"male":0, "female":1}
data = [train_data,test_data]
for dataset in data:
    dataset["Sex"] = dataset["Sex"].map(gender)

# TICKET
# drop this column because difficult to convert to numb
#print(train_data["Ticket"].head()) has 681 unique tickets so large to convert to numb'

train_data = train_data.drop(["Ticket"],axis=1)
test_data = test_data.drop(["Ticket"],axis=1)

# EMBARKED
port = {"S":0,"C":1,"Q":2}
data = [train_data,test_data]
for dataset in data:
    dataset["Embarked"] = dataset["Embarked"].map(port)


#Changing Currently Value

#Age - convert to Age Group => Easier to graph later
data = [train_data,test_data]
for dataset in data:
    dataset["Age"] = dataset["Age"].astype(int)
    dataset.loc[dataset["Age"] <= 11, "Age"] = 0
    dataset.loc[(dataset["Age"] > 11) & (dataset["Age"] <= 18), "Age"] = 1
    dataset.loc[(dataset["Age"] > 18) & (dataset["Age"] <= 22), "Age"] = 2
    dataset.loc[(dataset["Age"] > 22) & (dataset["Age"] <= 30), "Age"] = 3
    dataset.loc[(dataset["Age"] > 30) & (dataset["Age"] <= 40), "Age"] = 4
    dataset.loc[(dataset["Age"] > 40) & (dataset["Age"] <= 50), "Age"] = 5
    dataset.loc[(dataset["Age"] > 50) & (dataset["Age"] <= 60), "Age"] = 6
    dataset.loc[(dataset["Age"] > 60), "Age"] = 7

#print(train_data["Age"].value_counts())

# need to call data variable for every time do a for loop - due to the data at that moment has already been modify => using the latest data

# FARE - create Group value the same as Age
data = [train_data,test_data]
for dataset in data:
    dataset.loc[(dataset["Fare"] <= 7.91), "Fare"] = 0
    dataset.loc[(dataset["Fare"] > 7.91) & (dataset["Fare"] <= 14.454), "Fare"] = 1
    dataset.loc[(dataset["Fare"] > 14.454) & (dataset["Fare"] <= 31), "Fare"] = 2
    dataset.loc[(dataset["Fare"] > 31) & (dataset["Fare"] <= 99), "Fare"] = 3
    dataset.loc[(dataset["Fare"] > 99) & (dataset["Fare"] <= 251), "Fare"] = 4
    dataset.loc[(dataset["Fare"] > 251), "Fare"] = 5
    dataset["Fare"] = dataset["Fare"].astype(int)

# Create New Feature => Increase high accuracy

#Age vs Class
data = [train_data,test_data]
for dataset in data:
    dataset["Age_Class"] = dataset["Age"]*dataset["Pclass"]

#Fare/Person
data = [train_data,test_data]
for dataset in data:
    dataset["Fare_per_Person"] = dataset["Fare"] / (dataset["relatives"] +1)
    dataset["Fare_per_Person"] = dataset["Fare_per_Person"].astype(int)

#print(train_data.head(10))

#Building Algorithm Model

x_train = train_data.drop("Survived",axis=1)
y_train = train_data["Survived"]
x_test = test_data.iloc[:,1:]
#print(test_data.head())

#SGD Model
sgd = linear_model.SGDClassifier(max_iter=5,tol=None)
sgd.fit(x_train,y_train)
y_pred_sgd = sgd.predict(x_test)
sgd_score = sgd.score(x_train,y_train)
print("SGD Score:",sgd_score,round(sgd_score*100,2))

#Random Forest
rd = RandomForestClassifier(n_estimators=100)
rd.fit(x_train,y_train)
y_pred_rd = rd.predict(x_test)
rd_score = rd.score(x_train,y_train)
print("Random Forest Score:",rd_score,round(rd_score*100,2))

#SVC
svc = LinearSVC()
svc.fit(x_train,y_train)
y_pred_svc = svc.predict(x_test)
svc_score = svc.score(x_train,y_train)
print("Linear SVC Score:",svc_score,round(svc_score*100,2))

#KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
y_pred_knn = knn.predict(x_test)
knn_score = knn.score(x_train,y_train)
print("KNN Score:",knn_score,round(knn_score*100,2))

#Perceptron
pt = Perceptron(max_iter=5)
pt.fit(x_train,y_train)
y_pred_pt = pt.predict(x_test)
pt_score = pt.score(x_train,y_train)
print("Perceptron Score:",pt_score,round(pt_score*100,2))

#Decision Tree Classifier
tree = DecisionTreeClassifier()
tree.fit(x_train,y_train)
y_pred_tree = tree.predict(x_test)
tree_score = tree.score(x_train,y_train)
print("Decision Tree Classifier Score:",tree_score,round(tree_score*100,2))

#GaussianNB
nb = GaussianNB()
nb.fit(x_train,y_train)
y_pred_nb = nb.predict(x_test)
nb_score = nb.score(x_train,y_train)
print("GaussianNB Score:",nb_score,round(nb_score*100,2))

#Logistic Regression
log = LogisticRegression()
log.fit(x_train,y_train)
y_pred_log = log.predict(x_test)
log_score = log.score(x_train,y_train)
print("Logistic Regression Score:",log_score,round(log_score*100,2))

#Conclusion - best model
results = pd.DataFrame({"Model":["Support Vector Machines","KNN","Logistic Regression","Random Forest","Naive Bayes Gaussian","Perceptron","SGD","Decision Tree"],"Score":[round(log_score*100,2),round(knn_score*100,2),round(svc_score*100,2),round(rd_score*100,2),round(nb_score*100,2),round(pt_score*100,2),round(sgd_score*100,2),round(tree_score*100,2)]})
results_df = results.sort_values(by="Model", ascending=False)
results_df = results_df.set_index("Model")
print(results_df.head(9))


















