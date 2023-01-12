# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 03:11:21 2022

@author: xwtar
"""

import pandas as pd
import glob

path = 'C:/Users/xwtar/Documents/GitHub/Citations-Over-Year/Group4/Impact Score/*.csv'
csv_files = glob.glob(path)


df_list = []

# First year
x = 2012

for file in csv_files:    
    df = pd.read_csv(file)
    df = df.rename(columns={'Cites / Doc. (2years)': 'Impact Factor'})
    df['Impact Factor Year'] = x
    x = x + 1
    df_list.append(df)

df = pd.concat(df_list, ignore_index=True)
