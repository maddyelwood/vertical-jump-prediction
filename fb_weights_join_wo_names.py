#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from pandasql import sqldf

''' 
create a new df with all FOOTBALL players and their estimated weights,
then join using pandasql with the squat/vert dataset to then use in 
regression model 


manually type in id from teambuildr, weight, position

then join and continue
'''

#create new dataframe for football players
fb = {
    'ID': [
        '2395227',
        '2066958',
        '2437665',
        '1259227',
        '2395012',
        '1803704',
        '1686353',
        '1284517',
        '1686995',
        '2274432',
        '2979730',
        '1221941',
        '2238720',
        '1686349',
        '1722545',
        '2253051',
        '1221964',
        '1694621',
        '1059685',
        '1689652',
        '1812911',
        '1804679',
        '1688811',
        '2254257',
        '1686137',
        '2246388',
        '1710450',
        '1320707',
        '2271613',
        '1221982',
        '2452507',
        '2395218',
        '2253504',
        '1686089',
        '2280901',
        '1689539',
        '1689049',
        '2239261'
    ],
    'Position': [
       'QB',
       'QB',
       'WR',
       'RB',
       'DB',
       'QB',
       'WR',
       'RB',
       'DB',
       'DB',
       'DB',
       'LB',
       'DB',
       'LB',
       'RB',
       'LB',
       'LB',
       'DB',
       'DL',
       'FB',
       'LB',
       'DL',
       'DL',
       'LB',
       'OL',
       'OL',
       'OL',
       'OL',
       'OL',
       'OL',
       'WR',
       'WR',
       'WR',
       'TE',
       'TE',
       'WR',
       'DL',
       'DL'
    ],
    'Estimated_Weight': [
        195,
        155,
        155,
        190,
        170,
        185,
        190,
        205,
        185,
        160,
        165,
        170,
        165,
        180,
        165,
        195,
        185,
        175,
        240,
        190,
        205,
        200,
        230,
        220,
        225,
        250,
        280,
        275,
        260,
        300,
        170,
        150,
        165,
        200,
        225,
        160,
        250,
        220
    ]
}

fb_df = pd.DataFrame(fb)

all_df = pd.read_csv("imputed-data.csv")

query = """

SELECT fb_df.Position, fb_df.Estimated_Weight, all_df.*
FROM all_df
JOIN fb_df
ON all_df.ID = fb_df.ID

"""

all_fb = sqldf(query, globals())

print(all_fb)

all_fb.to_csv('fb_data_weights.csv')

