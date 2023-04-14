# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:44:25 2023

@author: wb578960
"""

import sqlite3
import pandas as pd

df = pd.read_csv('titanic.csv')

df.columns = df.columns.str.strip()

connection = sqlite3.connect('demo.db')

df.to_sql('titanic_data', connection, if_exists='replace') 

connection.close()
