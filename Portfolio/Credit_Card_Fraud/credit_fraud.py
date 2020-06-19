import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, precision_recall_curve, auc, make_scorer
from collections import Counter

data = pd.read_csv("creditcard.csv",sep=",")
print(data.head())
print(data.describe())
print(data.isnull().sum())
print(data.shape)

#31 column and 284807 values
#data has no null value
#Class split data 1 is fraud / 0 is normal

target = data["Class"]
counter = Counter(target)

for k,v in counter.items():
    per = v / len(target) * 100
    print("Class=",k,"Count=",v,"Percent=",per)




#Display the percentage of Fraud vs Missing Class
fraud_value_total = 0
normal_value_total = 0
for i in data["Class"]:
    if i == 1:
        fraud_value_total += 1
    elif i == 0:
        normal_value_total += 1
    else:
        pass

print("Total of Fraud is:",fraud_value_total)
print("Total of Normal is:",normal_value_total)


ax = sns.countplot(x="Class",data=data)
target = data["Class"]
histogram = data.hist(bins = 100)
for axis in histogram.flatten():
    axis.set_xticklabels([])
    axis.set_yticklabels([])

plt.show()

x = data.drop("Class",axis=1)
y = data["Class"]


def load_dataset(full_path):
    # load the dataset as a numpy array
    data = read_csv(full_path, header=None)
    # retrieve numpy array
    data = data.values
    # split into input and output elements
    X, y = data[:, :-1], data[:, -1]
    return X, y


# calculate precision-recall area under curve
def pr_auc(y_true, probas_pred):
    # calculate precision-recall curve
    p, r, _ = precision_recall_curve(y_true, probas_pred)
    # calculate area under curve
    return auc(r, p)


# evaluate a model
def evaluate_model(X, y, model):
    # define evaluation procedure
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    # define the model evaluation the metric
    metric = make_scorer(pr_auc, needs_proba=True)
    # evaluate model
    scores = cross_val_score(model, X, y, scoring=metric, cv=cv, n_jobs=-1)
    return scores


# define models to test
def get_models():
    models, names = list(), list()
    # CART
    models.append(DecisionTreeClassifier())
    names.append('CART')
    # KNN
    steps = [('s', StandardScaler()), ('m', KNeighborsClassifier())]
    models.append(Pipeline(steps=steps))
    names.append('KNN')
    # Bagging
    models.append(BaggingClassifier(n_estimators=100))
    names.append('BAG')
    # RF
    models.append(RandomForestClassifier(n_estimators=100))
    names.append('RF')
    # ET
    models.append(ExtraTreesClassifier(n_estimators=100))
    names.append('ET')
    return models, names


# define the location of the dataset
full_path = 'creditcard.csv'
# load the dataset
X, y = load_dataset(full_path)
# define models
models, names = get_models()
results = list()
# evaluate each model
for i in range(len(models)):
    # evaluate the model and store results
    scores = evaluate_model(X, y, models[i])
    results.append(scores)
    # summarize performance
    print('>%s %.3f (%.3f)' % (names[i], mean(scores), std(scores)))
# plot the results
plt.boxplot(results, labels=names, showmeans=True)
pyplot.show()


