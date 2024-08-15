#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import RFE

data = pd.read_csv('vb_data_weights.csv')

# split data into features and target
X = data.drop(['First', 'Last', 'ID', 'Vert', 'Position'], axis=1)
y = data['Vert']

# split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# define model
#model = RandomForestRegressor(random_state=42)
model = Ridge(alpha=1.0)

# use grid search to find best parameters for model
'''
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
print(f'best params: {best_params}')


# train model with params found
model = grid_search.best_estimator_
'''

# feature selection using RFE (recursive feature elimination)
#selector = RFE(model, n_features_to_select=5, step=1)
#selector = selector.fit(X_train, y_train)

#features = X_train.columns[selector.support_]
#print(f'selected features: {features}')

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
feature_names = ['BSS', 'BS', 'Clean', 'Estimated_Weight']
with open('vb_vert_predictor.pkl', 'wb') as f:
    pickle.dump((model, feature_names), f)
    

