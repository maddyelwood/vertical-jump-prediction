#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
I want to assign all players in the vb dataset a categorical variable of
gender that is set to 0 for female.

Then I want to assign all players in the fb dataset the same variable 
but set to 1.

Last I will combine these two datasets together to create a new dataset of 
athletes' max info with weights and specified gender to then use in a new
program to build a new model.
'''

import pandas as pd
import pandasql as psql

# load in vb dataset
vb_df = pd.read_csv('vb_data_weights.csv')

# define value for new column
gender_val = '0'

# create sql query to add new gender column
query = f"""
    SELECT *, '{gender_val}' AS Gender
    FROM vb_df
"""

# execute query
vb_df = psql.sqldf(query, locals())

#print(vb_df.head())

######### NOW DO SAME FOR FOOTBALL #########
# load in dataset
fb_df = pd.read_csv('fb_data_weights.csv')

# define value for new column
gender_val = '1'

# create sql query
query = f"""
    SELECT *, '{gender_val}' AS Gender
    FROM fb_df
"""

# execute query!
fb_df = psql.sqldf(query, locals())

#print(fb_df.head())

######### NOW CONNECT BOTH DFs #########
# align columns of both dataframes (make sure they have similar columns)
common_columns = vb_df.columns.intersection(fb_df.columns)

vb_df = vb_df[common_columns]
fb_df = fb_df[common_columns]

query = """ 
    SELECT * FROM vb_df
    UNION ALL
    SELECT * FROM fb_df
"""

union_df = psql.sqldf(query, locals())

print(union_df)

union_df.to_csv('athlete-data-with-weights.csv')