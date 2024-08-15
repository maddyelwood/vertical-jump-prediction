#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pickle
import numpy as np

# load pickled model
#with open('vb_vert_predictor.pkl', 'rb') as file:
#    model, feature_names = pickle.load(file)

# with open('vert_predictor.pkl', 'rb') as file:
#     model, feature_names = pickle.load(file)

#with open('fb_vert_predictor.pkl', 'rb') as file:
#    model, feature_names = pickle.load(file)

with open('athlete_vert_predictor.pkl', 'rb') as file:
    model, feature_names = pickle.load(file)
    
#with open('athlete_vert_predictor.pkl', 'rb') as file:
#    model, poly, feature_names = pickle.load(file)


def get_prediction(features):
    # takes list of features and returns prediction from model
    feature_array = np.array(features).reshape(1, -1)
    prediction = model.predict(feature_array)
    return prediction[0]


''' uncomment if poly model
def get_prediction(features):
    feature_array = np.array(features).reshape(1, -1)
    feature_array_poly = poly.transform(feature_array)
    prediction = model.predict(feature_array_poly)
    return prediction[0]
'''

while True:
    input_features = []
    for feature_name in feature_names:
        feature_value = float(input(f'Enter value for {feature_name}: '))
        input_features.append(feature_value)
    
    prediction = get_prediction(input_features)
    
    print(f"2-legged Vertical Prediction: {prediction:.2f} inches")
    
    # ask for another prediction
    again = input("Would you like to make another prediction? (yes/no): ").strip().lower()
    if again != 'yes':
        break
    
