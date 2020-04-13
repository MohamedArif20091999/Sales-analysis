# -*- coding: utf-8 -*-
"""Bigmart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UeMtN72AS8yrkISmBnmjAy30MvSpbzcc
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

data=pd.read_csv("/content/gdrive/My Drive/big-mart-sales-prediction/Train.csv")

data.head()

data.shape

data.describe()

for colm in data.columns:    #COLUMN NAMES
  print(colm)

data.info()

plt.boxplot(data.Item_Outlet_Sales)
plt.show()

plt.hist(data.Item_Outlet_Sales)
plt.plot()

desc=data.Item_Outlet_Sales
desc.describe()

data.Item_Identifier

data.shape

data.drop('Item_Identifier', axis=1, inplace=True)

data.shape

data.info()



"""ATTACKING ONE BY  ONE

```
# This is formatted as code
```
"""

def nullcheck(colname,s):
  cou=colname.isnull().values.sum()
  print("NULL COUNT of  "+s+":",cou)
  return

nullcheck(data['Item_Weight'], 'Item_Weight') 
nullcheck(data['Item_Fat_Content'],'Item_Fat_Content')    
nullcheck(data['Item_Visibility'],'Item_Visibility')     
nullcheck(data['Item_Type'],'Item_Type')  
nullcheck(data['Item_MRP'],'Item_MRP')               
nullcheck(data['Outlet_Identifier'],'Outlet_Identifier')   
nullcheck(data['Outlet_Establishment_Year'],'Outlet_Establishment_Year')  
nullcheck(data['Outlet_Size'],'Outlet_size')       
nullcheck(data['Outlet_Location_Type'],'Outlet_Location_Type') 
nullcheck(data['Outlet_Type'],'Outlet_type') 
nullcheck(data['Item_Outlet_Sales'],'Item_outlrt_sales')

data['Item_Weight'] = data['Item_Weight'].fillna((data['Item_Weight'].mean()))

data['Item_Weight'].head(3)

data.info()

#NEXT IS OUTLET SIZE.
data['Outlet_Size'].head()

data['Outlet_Size']=data['Outlet_Size'].fillna(data['Outlet_Size'].mode()[0])

data['Outlet_Size'].head()

data.info()

data.Outlet_Size.value_counts()

def category_count(column):
    return column.value_counts()

print(category_count(data['Item_Fat_Content']))
print("|||||||||| END ||||||||||")
print(category_count(data['Item_Type']))
print("|||||||||| END ||||||||||")
print(category_count(data['Outlet_Identifier']))
print("|||||||||| END ||||||||||")
print(category_count(data['Outlet_Size']))
print("|||||||||| END ||||||||||")
print(category_count(data['Outlet_Location_Type']))
print("|||||||||| END ||||||||||")
print(category_count(data['Outlet_Type']))
print("|"*10 +" END " +"|"*10)

data=pd.get_dummies(data,columns=['Item_Fat_Content' ,'Item_Type','Outlet_Identifier','Outlet_Size','Outlet_Location_Type','Outlet_Type'],drop_first=True)

data.shape

data.head(10)



"""CREATE MODEL:"""

data.head(2)

data.describe().T

data.info()

data.iloc[5].values

data.head()

data['Outlet_Establishment_Year'].value_counts()

data=pd.get_dummies(data,columns=['Outlet_Establishment_Year'],drop_first=True)

data.shape

data.info()

Data=data

Data.head()

X= Data.drop(['Item_Outlet_Sales'], axis=1)
X.shape

Y=Data['Item_Outlet_Sales']
Y.shape

Y.head()

X.head()

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

from sklearn.linear_model import LinearRegression
regression=LinearRegression()
model_linreg=regression.fit(X_train,Y_train)

print(model_linreg.intercept_)
print(model_linreg.coef_)

from sklearn.metrics import mean_squared_error
predicts=model_linreg.predict(X_test)
pre_MSE=mean_squared_error(Y_test,predicts)
pre_rMSE=np.sqrt(pre_MSE)
pre_rMSE

data['Item_Outlet_Sales'].describe()

Y_test.head(10)

model_linreg.predict(X_test)[4]

data.iloc[[944]]



"""DECISION TREE:"""

from sklearn.tree import DecisionTreeRegressor
dtree=DecisionTreeRegressor(random_state=0)
model_dtree=dtree.fit(X_train,Y_train)

preds=model_dtree.predict(X_test)
tree_mse=mean_squared_error(Y_test,preds)
tree_rmse=np.sqrt(tree_mse)
tree_rmse

from sklearn import tree
import pydotplus
from IPython.display import Image

dot_d=tree.export_graphviz(dtree,out_file=None)
graph=pydotplus.graph_from_dot_data(dot_d)
Image(graph.create_png())



"""RANDOM FOREST:"""

from sklearn.ensemble import RandomForestRegressor
raf=RandomForestRegressor(random_state=0,n_jobs=-1,n_estimators=10)
modell=raf.fit(X_train,Y_train)

pred=modell.predict(X_test)
raf_mse=mean_squared_error(Y_test,pred)
raf_rmse=np.sqrt(raf_mse)
raf_rmse

from sklearn.model_selection import cross_val_score
scores=cross_val_score(raf,X_test,Y_test,scoring="neg_mean_squared_error",cv=10)
scores=np.sqrt(-scores)

scores

