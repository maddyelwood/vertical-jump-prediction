#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import pandasql as psql
pysqldf = lambda query: psql.sqldf(query, globals())

data1 = pd.read_csv('Squat and Jumps Max Report.csv', encoding='latin1', header=0)
data2 = pd.read_csv('clean-maxes.csv', encoding='latin1', header=0)

# dropping average row at bottom of both df
data1 = data1.drop(data1.index[-1])
data2 = data2.drop(data2.index[-1])

# CHANGE THE NAMES TO NOT HAVE SPACES BEFORE DOING ANYTHING
data1 = data1.rename(columns={
    'Rear Foot Elevated SL Vertical Jump (Left) Testing' : 'SLVl',
    'Rear Foot Elevated SL Vertical Jump (Right) Testing' : 'SLVr',
    'Bulgarian Split Squat' : 'BSS',
    'Back Squat' : 'BS',
    'Vertical Jump (Testing)' : 'Vert',
    'User ID' : 'ID'
    })

data2 = data2.rename(columns={
    'User ID' : 'ID'
    })

# print(data1.head())
# print(data2.head())


#note: first tried without the {} and got the error
#then tried with actual long string and still got error
#says it is syntax erroring around "Elevated"
query = f'''
    SELECT  data1.ID,
            data1.First,
            data1.Last,
            data1.SLVl, 
            data1.SLVr, 
            data1.BSS, 
            data1.BS, 
            data1.Vert, 
            data2.Clean
    FROM data1
    JOIN data2 ON data1.ID = data2.ID
    '''

joined_data = pysqldf(query)

joined_data = joined_data[joined_data['ID'] != 2698950.0]

print(joined_data)

joined_data.to_csv('squats-cleans-data.csv')

# removing obviously entered mistake... i wonder if we could write code to 
# detect this if didn't already know (outlier detection for mis-input)
# data1 = data1[data1['User ID'] != 2698950]
# data2 = data2[data2['User ID'] != 2698950]

