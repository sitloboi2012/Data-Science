import json
import ast
import pandas as pd
import csv
import re

with open("bimbim-pwa-UserOrder-export.json", encoding="utf-8") as json_file:
    data = json.load(json_file)

collectType = []
shopName = []
Location = []
name = []
#stuffName = []
shipperName = []
shopTotal = []
status = []
timeCollect = []
paymentType = []

for i in data:
    for j in data[i]:

        # collect group
        if j == "collect":
            for x in data[i][j]:
                if "collect" in x.keys():
                    value = x.get("collect")
                    collectType.append(value)
                else:
                    pass

                if "name" in x.keys():
                    value = x.get("name")
                    shopName.append(value)
                else:
                    pass
        else:
            pass

        # location part
        if j == "location":
            Location.append(data[i][j])
        else:
            pass

        # name part
        if j == "name":
            name.append(data[i][j])
        else:
            pass

        if j == "payment":
            paymentType.append(data[i][j])
        else:
            pass


        # amount / shipper / shoptotal / total/status part
        if j == "order":
            for x in data[i][j]:
                for a in data[i][j][x]:

                    # Shipper part
                    if a == "Shipper":
                        shipperName.append(data[i][j][x][a])
                    else:
                        pass

                    if a == "shopTotal":
                        shopTotal.append(data[i][j][x][a])
                    else:
                        pass

                    if a == "status":
                        status.append(data[i][j][x][a])
                    else:
                        pass

                    if a == "timeCollect":
                        timeCollect.append(data[i][j][x][a])
                    else:
                        pass


"""print(len(collectType)) #1
print(len(shopName)) #2
print(len(Location)) #a
print(len(name)) #b
print(len(shipperName))
print(len(timeCollect)) #3
print(len(shopTotal)) #4
print(len(status)) #5
print(len(paymentType)) #c"""


data = {"Collect Type":collectType,
         "Shop Name":shopName,
         "Time Collect":timeCollect,
         "Shop Total":shopTotal,
         "Status Type":status}

data_list = [
    ["Name","Location","Shop Name","Time Buying","Collect Type","Total Money","Shipper","Status","Payment Type"]
]


rows = zip(name,Location,shopName,timeCollect,collectType,shopTotal,shipperName,status,paymentType)


#with open("DataSale.csv","w",newline="",encoding="utf-8") as data_csv:
 #   writer = csv.writer(data_csv)
  #  for row in rows:
   #     writer.writerow(row)


#df = pd.DataFrame(data=data,columns=["Collect Type","Shop Name","Time Collect","Shop Total","Status Type"])
#print(df.head())

for i in shopName:
    x = re.search("^Ăn Vặt.*CBD$",i)
    if x:
        print(i)
    else:
        pass

print(shopName)


#Croydon (Croydon park) + Woodville + Mansfield Park + Woodville South + Pennington + West Croydon + Woodville North + Ferryden Park + Regency Park + Woodville Garden + Kilkenny

