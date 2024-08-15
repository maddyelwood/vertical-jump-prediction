#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('fb_data_weights.csv')

# split data into features and target
X = data.drop(['First', 'Last', 'ID', 'Vert', 'Position', 'SLVl', 'SLVr'], axis=1)
y = data['Vert']

# split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# define model
model = Ridge(alpha=1.0)

# train new model using selected features
features = ['BSS', 'BS', 'Clean', 'Estimated_Weight']

X_train = X_train[features]
X_test = X_test[features]

model.fit(X_train, y_train)

# evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse}')
print(f'R^2 score: {r2}')

cv_scores = cross_val_score(model, X_train, y_train, cv=5)
print(f'cross-val mse: {-np.mean(cv_scores)}')

# pickle model
feature_names = ['BSS', 'BS', 'Clean', 'Weight']
with open('fb_vert_predictor.pkl', 'wb') as f:
    pickle.dump((model, feature_names), f)
    

