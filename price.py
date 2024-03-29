import pandas as pd
import numpy as np

data = pd.read_csv('/Users/venug/OneDrive/Desktop/House price/train.csv')

data.head()

data.shape

data.info()

for column in data.columns:
    print(data[column].value_counts())
    print("*"*20)

data.isna().sum()

data.drop(columns=['lot_size','lot_size_units'],inplace=True)

data.describe()

data.info()

data['beds'].value_counts()

data.head()

data['price_per_sqft'] = data['price'] * 100000 / data['size']

data['price_per_sqft']

data.describe()

data.shape

data

data.drop(columns=['size_units'],inplace=True)

data

data.drop(columns=['price_per_sqft'],inplace=True)

data.head()

data.to_csv("final_dataset.csv")

X=data.drop(columns=['price'])
y=data['price']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=0)

print(X_train.shape)
print(y_train.shape)

column_trans = make_column_transformer((OneHotEncoder(sparse=False), ['beds']), remainder='passthrough')

scaler = StandardScaler()

lr = LinearRegression(normalize=True)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

lr = LinearRegression()
lr.fit(X_scaled, y)

pipe = make_pipeline(column_trans,scaler, lr)

pipe.fit(X_train,y_train)

y_pred_lr = pipe.predict(X_test)

r2_score(y_test,y_pred_lr)

lasso = Lasso()
pipe = make_pipeline(column_trans,scaler, lasso)
pipe.fit(X_train,y_train)

y_pred_lasso = pipe.predict(X_test)
r2_score(y_test,y_pred_lasso)

ridge = Ridge()
pipe = make_pipeline(column_trans,scaler, ridge)
pipe.fit(X_train,y_train)

y_pred_ridge = pipe.predict(X_test)
r2_score(y_test,y_pred_ridge)

print("No Regularization: ", r2_score(y_test,y_pred_lr))
print("Lasso: ", r2_score(y_test,y_pred_lasso))
print("Ridge: ", r2_score(y_test,y_pred_ridge))
