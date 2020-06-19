import numpy as np
import pandas as pd
import sklearn
import seaborn as sns
import bimbim_json
import re
import matplotlib.pyplot as plt
from sklearn import linear_model,preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("DataSale.csv",sep=",",header=None)
data.columns = ["Name","Location","Shop Name","Time Buying","Collect Type","Total Money","Shipper","Status","Payment Type"]
print(data.head())
print(data.describe())
#print(data.isnull().sum())

data = data.dropna()

#print(data["Shop Name"].value_counts(sort=True))

for i in data["Shop Name"]:
    x = re.search("^Ăn Vặt",i)
    if x:
        print(i)
    else:
        pass

print(data["Shop Name"])



