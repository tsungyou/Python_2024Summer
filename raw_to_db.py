from datetime import datetime, timedelta
import pandas as pd
import os
from config import *
csvs = os.listdir(raw_data_path)
list_ = []
for fname in csvs:
    df = pd.read_csv(raw_data_path + fname)
    list_.append(df)

dir_weekday = {"Monday": 1,
               "Tuesday": 2,
               "Wednesday": 3,
               "Thursday": 4,
               "Friday": 5,
               "Saturday": 6,
               "Sunday": 7}
now = datetime.now()
for df in list_: 
    df['dt'] = df['Day'].apply(lambda x: (now - timedelta(now.weekday()-dir_weekday[x]+1)).strftime("%Y-%m-%d"))
final = pd.concat(list_)
final.to_csv(target_data_path + "final.csv")