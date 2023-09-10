#imports for ML
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # to split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier #our classifier 
from sklearn.metrics import accuracy_score, roc_curve, auc #metric 
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn import tree
from sklearn.metrics import f1_score
import os
#read from same folder
books = 'booksdata.json'
if os.path.isfile(books):
    books = pd.read_json(books)
else:
    print(f"Error: {books} not found in the current directory.")
    exit()

y_variable = books.price
y_variable = pd.DataFrame(y_variable)
data = books.drop(columns= ['price'])
data = data.drop(columns=['url','title', 'description'])
#write out some machine learning algo 
machine_algo_1 = ['DT', 'RF'] #decision tree, logistic regression, linear regression
metrics_to_measure = ['accuracy', 'roc_auc']

#select the respective variables
continuous_variables = data.select_dtypes(include=['int', 'float']).columns.tolist()
categorical_variables =data.select_dtypes(include  = ['object']).columns.tolist()

#first iteration of simple linear regression
dummies=pd.get_dummies(data[categorical_variables], prefix=categorical_variables, drop_first=True)
data = pd.concat([data.drop(columns=categorical_variables), dummies], axis=1)
X = data
y = y_variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

reg = LinearRegression().fit(X, y)
reg.score(X, y)
reg = reg.score(X, y)
max_score = reg 
best_model = 'linear_regression'



print(f' the best model is {best_model} with a max score of {max_score}')
