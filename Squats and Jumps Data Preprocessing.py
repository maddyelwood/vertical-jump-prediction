#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this program is preprocessing on a data file containing
all athletes in teambuildr's max squat, bulgarian split squat,
single leg verticals (L & R), and normal verticals
    
listwise deletion of athletes without info for all 5 categories

"""
import pandas as pd

data = pd.read_csv('Squat and Jumps Max Report.csv', encoding='latin1', header=0)
#print(data)


# last row of file is avg of all athletes, so remove this row in dataframe
data = data.drop(data.index[-1])

# removing obvious input mistake of 20000+ lbs squat max
data = data[data['User ID'] != 2698950]

# calculate number of missing values per column
missingValues = data.isnull().sum()
missingValuesReport = pd.DataFrame(missingValues, columns=['Missing Values'])
#print(missingValuesReport)


# now remove those rows with null values
# dataCleaned = data.dropna()

# print(dataCleaned)

'''
after this, data went from 357 athletes, to 64 athletes that had all this info.
trying again with separate dataframes for different lifts
'''

# SScolumns = ['Rear Foot Elevated SL Vertical Jump (Right) Testing',
#              'Rear Foot Elevated SL Vertical Jump (Left) Testing',
#              'Bulgarian Split Squat'
#              ]

# BScolumns = ['Vertical Jump (Testing)', 'Back Squat']

'''
possibly going to edit this previous section later if wanting to look at
SS vs Normal Vert or BS vs SL Vert
'''

# dataSS = data.dropna(subset=SScolumns)
# dataBS = data.dropna(subset=BScolumns)

# print(dataSS) # ended up with 94 athletes left
# print(dataBS) # ended up with 146 athletes left

# dataSS.to_csv('SS and SL Vert Data.csv')
# dataBS.to_csv('BS and Vert Data.csv')

''' 
now testing different imputation techniques
'''

# first trying mode
# for column in data.columns:
#     modeValue = data[column].mode()[0]
#     data[column].fillna(modeValue, inplace=True)

# missingValues = data.isnull().sum()
# missingValuesReport = pd.DataFrame(missingValues, columns=['Missing Values'])
# print(missingValuesReport)

# data.to_csv('modeFilledData.csv')

# next trying mean
# for column in data.columns:
#     # only calc & fill numerical columns (NOT NAMES)
#     if data[column].isnull().sum() > 0 and data[column].dtype in ['float64', 'int64']:
#         meanValue = data[column].mean()
#         data[column].fillna(meanValue, inplace=True)

# missingValues = data.isnull().sum()
# missingValuesReport = pd.DataFrame(missingValues, columns=['Missing Values'])
# print(missingValuesReport)

# data.to_csv('meanFilledData.csv')

for column in data.columns:
    # only calc & fill numerical columns (NOT NAMES)
    if data[column].isnull().sum() > 0 and data[column].dtype in ['float64', 'int64']:
        medianValue = data[column].median()
        data[column].fillna(medianValue, inplace=True)

missingValues = data.isnull().sum()
missingValuesReport = pd.DataFrame(missingValues, columns=['Missing Values'])
print(missingValuesReport)

print(data.head())

data.to_csv('medianFilledData.csv')