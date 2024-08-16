#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from pandasql import sqldf

''' 
create a new df with all volleyball players and their estimated weights,
then join using pandasql with the squat/vert dataset to then use in 
regression model 


manually type in id from teambuildr, weight, position

then join and continue
'''

#create new dataframe for volleyball players
vb = {
    'ID': [
        '1464092', 
        '2243732',
        '2255050',
        '1684819',
        '2241564',
        '2244018',
        '2820629',
        '2242929',
        '2241568',
        '1697144',
        '2241616',
        '2245886',
        '2241536',
        '1685252'
    ],
    'Position': [
        'MB',
        'S',
        'DS',
        'DS',
        'S',
        'MB',
        'S',
        'MB',
        'MB',
        'OH',
        'DS',
        'OH',
        'MB',
        'MB'
    ],
    'Estimated_Weight': [
        155, 
        130,
        125,
        125,
        130,
        155,
        130,
        155,
        155,
        140,
        125,
        140,
        155,
        155
    ]
}

vb_df = pd.DataFrame(vb)

all_df = pd.read_csv("imputed-data.csv")

query = """

SELECT vb_df.Position, vb_df.Estimated_Weight, all_df.*
FROM all_df
JOIN vb_df
ON all_df.ID = vb_df.ID

"""

all_vb = sqldf(query, globals())

print(all_vb)

all_vb.to_csv('vb_data_weights.csv')