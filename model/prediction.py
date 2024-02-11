import pandas as pd
import numpy as np

## Importing the data
dataset = pd.read_csv('Data.csv')
dataset.iloc[:,:4] = dataset.iloc[:,:5].fillna('Unknown')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

## Handling Missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 5:])
X[:, 5:] = imputer.transform(X[:, 5:])

## Encoding the Categorical data
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
column_transformer = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0,1,2,3])],
                                       remainder='passthrough')
column_transformer.fit(X)
X = np.array(column_transformer.transform(X))

## Fitting the Random Forest Regressor Model
from sklearn.ensemble import RandomForestRegressor
rf_regressor =  RandomForestRegressor(n_estimators = 1000, random_state=123)
rf_regressor.fit(X, y)

def predictResult(data):
    data = np.array(data).reshape(1,12)
    data = np.array(column_transformer.transform(data))
    result =  rf_regressor.predict(data)
    return int(result)
