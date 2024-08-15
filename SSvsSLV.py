#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:04:02 2024

@author: maddyelwood
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# read in data from csv using pandas
#data = pd.read_csv('max-report.csv', header=0)
#data = pd.read_csv('SS and SL Vert Data.csv')
#data = pd.read_csv('modeFilledData.csv')
#data = pd.read_csv('meanFilledData.csv')
data = pd.read_csv('medianFilledData.csv')
print(data)

# key for repeated long strings:
SLVl = "Rear Foot Elevated SL Vertical Jump (Left) Testing"
SLVr = "Rear Foot Elevated SL Vertical Jump (Right) Testing"
BSS = "Bulgarian Split Squat"

# data cleaning:
# remove "-", remove inches label from integers, turn into float values
'''
this section was only needed when using softball only data.
with new csv file containing all athletes, not necessary.
'''
# data = data[~data.isin(["-"]).any(axis=1)]
# data['Bulgarian Split Squat'] = data['Bulgarian Split Squat'].astype(float)
# data['Rear Foot Elevated SL Vertical Jump (Right) Testing'] = data['Rear Foot Elevated SL Vertical Jump (Right) Testing'].str.replace('"', '').astype(float)
# data['Rear Foot Elevated SL Vertical Jump (Left) Testing'] = data['Rear Foot Elevated SL Vertical Jump (Left) Testing'].str.replace('"', '').astype(float)
# print(data['Rear Foot Elevated SL Vertical Jump (Left) Testing'])

# scatter plot of rl vs max
# plt.scatter(data['Rear Foot Elevated SL Vertical Jump (Right) Testing'], data['Bulgarian Split Squat'])
# plt.xlabel('Right Leg Jump (inches)')
# plt.ylabel('Bulgarian Split Squat (pounds)')
# plt.title('Right Leg Vertical v. Split Squat Max')
# plt.show()

# scatter plot of ll vs max
# plt.scatter(data['Rear Foot Elevated SL Vertical Jump (Left) Testing'], data['Bulgarian Split Squat'])
# plt.xlabel('Left Leg Jump (inches)')
# plt.ylabel('Bulgarian Split Squat (pounds)')
# plt.title('Left Leg Vertical v. Split Squat Max')
# plt.show()

# create x and y for linear regression model
X = data[[BSS]] # features
y = data[[SLVl, SLVr]] # targets (checking both legs)

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create and train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions using test set
y_pred = model.predict(X_test)

# evaluate model
mse_ll = mean_squared_error(y_test[SLVl], y_pred[:, 0])
r2_ll = r2_score(y_test[SLVl], y_pred[:, 0])
mse_rl = mean_squared_error(y_test[SLVr], y_pred[:, 1])
r2_rl = r2_score(y_test[SLVr], y_pred[:, 1])

print("Linear Regression on all athletes with SS and SLV info:")
print(f'Mean Squared Error (LL results): {mse_ll}')
print(f'R^2 Score (LL results): {r2_ll}')
print(f'Mean Squared Error (RL results): {mse_rl}')
print(f'R^2 Score (RL results): {r2_rl}')

# plot results
plt.scatter(X_test, y_test[SLVl], color='blue', label='Actual')
plt.scatter(X_test, y_pred[:, 0], color='red', label='Predicted')
plt.xlabel(f'{BSS} (pounds)')
plt.ylabel(f'{SLVl} (inches)')
plt.legend()
plt.show()

plt.scatter(X_test, y_test[SLVr], color='blue', label='Actual')
plt.scatter(X_test, y_pred[:, 1], color='red', label='Predicted')
plt.xlabel(f'{BSS} (pounds)')
plt.ylabel(f'{SLVr} (inches)')
plt.legend()
plt.show()


