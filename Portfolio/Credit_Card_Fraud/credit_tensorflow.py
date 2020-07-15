import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import BatchNormalization,Dropout,Dense,Flatten,Conv1D
from tensorflow.keras.optimizers import Adam

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#load data
original_data = pd.read_csv("creditcard.csv",sep=",")

#data information
"""original_data.head()
original_data.info()
original_data.describe()
original_data.isnull().sum
original_data.shape"""

#Count "Class" number
print(original_data.Class.value_counts())

#Create a new dataframe to decreasing the unbalancing of data
fraud = original_data[original_data["Class"] == 1]
normal = original_data[original_data["Class"] == 0]

#get random sample from original data
#as we can see that there is 492 sample is Fraud so we want the Normal also has the same number 492
not_fraud = normal.sample(492)

balance_data = fraud.append(not_fraud,ignore_index=True)

print(balance_data.Class.value_counts())

x = balance_data.drop(["Class"],axis=1)
y = balance_data["Class"]

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0,test_size=0.3)

#apply Standard Scaler to obtain all features in similar range
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

#Convert to 3D shape for tensorflow
x_train = x_train.reshape(x_train.shape[0],x_train.shape[1],1)
x_test = x_test.reshape(x_test.shape[0],x_test.shape[1],1)

#Sequential Model
model = Sequential()
model.add(Conv1D(32,2,activation="relu",input_shape=x_train[0].shape))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Conv1D(64,2,activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(64,activation="relu"))
model.add(Dropout(0.5))

model.add(Dense(1,activation="sigmoid"))

#print(model.summary())

#Fitting and Compilling
model.compile(optimizer=Adam(learning_rate=0.0001), loss="binary_crossentropy",metrics=["accuracy"])

history = model.fit(x_train,y_train,epochs=20,validation_data=(x_test,y_test))

#plot the Learning Curve out
def plotLearningCurve(history,epochs):
  epochRange = range(1,epochs+1)
  plt.plot(epochRange,history.history['accuracy'])
  plt.plot(epochRange,history.history['val_accuracy'])
  plt.title('Model Accuracy')
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.legend(['Train','Validation'],loc='upper left')
  plt.show()

  plt.plot(epochRange,history.history['loss'])
  plt.plot(epochRange,history.history['val_loss'])
  plt.title('Model Loss')
  plt.xlabel('Epoch')
  plt.ylabel('Loss')
  plt.legend(['Train','Validation'],loc='upper left')
  plt.show()

plotLearningCurve(history,20)