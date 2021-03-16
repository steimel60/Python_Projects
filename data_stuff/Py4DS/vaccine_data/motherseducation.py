import pandas as pd
import numpy as np
from os import path


this_folder = path.dirname(__file__)
df = pd.read_csv(path.join(this_folder, 'NISPUF17.csv'))

less_than_high = pd.Series(df['EDUC1'] == 1).sum()
high = pd.Series(df['EDUC1'] == 2).sum()
more_than_high = pd.Series(df['EDUC1'] == 3).sum()
college = pd.Series(df['EDUC1'] == 4).sum()
total = len(pd.Series(df['EDUC1']))

list = [less_than_high, high, more_than_high, college, total]

proportions = [x/total for x in list]

#print(proportions)

dict = {"less than high school": proportions[0],
        "high school": proportions[1],
        "more than high school but not college": proportions[2],
        "college": proportions[3]}

print(dict)
