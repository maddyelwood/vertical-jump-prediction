#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

data = pd.read_csv('squats-cleans-data.csv')

# remove weird numbered column
data = data.drop(data.columns[0], axis=1)

# calculate number of missing values per column
missingValues = data.isnull().sum()
missingValuesReport = pd.DataFrame(missingValues, columns=['Missing Values'])
#print(missingValuesReport)

# figure out which columns need/don't need imputation
constant_columns = ['First', 'Last', 'ID']
data_not_imputed = data[constant_columns]

data_for_imputation = data.drop(columns=constant_columns)

# initialize imputer
imputer = IterativeImputer()

# fit and transform data with imputer
data_imputed = imputer.fit_transform(data_for_imputation)
data_imputed = pd.DataFrame(data_imputed, columns=data_for_imputation.columns)

# combine imputed with non-imputed
final_data = pd.concat([data_not_imputed.reset_index(drop=True), data_imputed.reset_index(drop=True)], axis=1)

print(final_data.head())

final_data.to_csv('imputed-data.csv')