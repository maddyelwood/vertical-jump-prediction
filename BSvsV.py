#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

#data = pd.read_csv('BS and Vert Data.csv')
#data = pd.read_csv('modeFilledData.csv')
#data = pd.read_csv('meanFilledData.csv')
data = pd.read_csv('medianFilledData.csv')
#print(data)

BS = "Back Squat"
Vt = "Vertical Jump (Testing)"

# create x and y for linear regression model
X = data[[BS]] # feature
y = data[Vt] # target 

#max_value = data[BS].max()
#max_value_index = data[data[BS] == max_value].index

#data = data.drop(max_value_index)
#print(data)

'''
The previous 4 lines of code removed an obvious outlier/input error
from someone supposedly squatting 214704 pounds... however removing this
did not impact the result in the end at all :/ 
'''

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create and train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# trying ridge regression
# ridgeModel = Ridge(alpha=1.0)
# ridgeModel.fit(X_train, y_train)

# trying lasso regression
#lasso_model = Lasso(alpha=0.1)
#lasso_model.fit(X_train, y_train)

# make predictions using test set
y_pred = model.predict(X_test)
# y_pred_ridge = ridgeModel.predict(X_test)
#y_pred_lasso = lasso_model.predict(X_test)

# evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# mse_ridge = mean_squared_error(y_test, y_pred_ridge)
# r2_ridge = r2_score(y_test, y_pred_ridge)

#mse_lasso = mean_squared_error(y_test, y_pred_lasso)
#r2_lasso = r2_score(y_test, y_pred_lasso)


print("Linear Regression on all athletes with BS and Vertical info:")
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# print("Ridge Regression info:")
# print(f'Mean Squared Error: {mse_ridge}')
# print(f'R^2 Score: {r2_ridge}')

#print("Lasso Regression info:")
#print(f'Mean Squared Error: {mse_lasso}')
#print(f'R^2 Score: {r2_lasso}')

# plot results
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Linear Prediction')
# plt.plot(X_test, y_pred_ridge, color='green', linewidth=2, label='Ridge Prediction')
#plt.plot(X_test, y_pred_lasso, color='yellow', linewidth=2, label='Lasso Prediction')
plt.xlabel(f'{BS} (pounds)')
plt.ylabel(f'{Vt} (inches)')
plt.legend()
plt.show()


'''
Trying ridge and lasso results in the same exact thing since 
we only have one feature at the moment.
'''