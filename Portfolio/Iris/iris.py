import numpy as np 
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import accuracy_score,r2_score


data = pd.read_csv('iris.data',sep=",")
print(data.describe())


target = data["class"]

#count the target
"""print(data['class'].value_counts())"""

#testing missing values
"""train_missing = data.isnull().sum()
print(train_missing)"""

le = preprocessing.LabelEncoder()
data["class"] = le.fit_transform(data["class"])

x = np.array(data.drop(["class"],1))
y = np.array(data["class"])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

model = LinearRegression()
model.fit(x_train,y_train)
acc = model.score(x_train,y_train)
y_pred = model.predict(x_test)

print("Coefficent: ",model.coef_)
print("Intercept: ",model.intercept_)

print("Accuracy Score:",acc)

for i in range(len(y_pred)):
    print("Predicted: ",int(y_pred[i]))
    print("Actual: ",y_test[i])





