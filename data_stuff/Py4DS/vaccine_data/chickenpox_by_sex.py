import pandas as pd
import numpy as np
from os import path


this_folder = path.dirname(__file__)
df = pd.read_csv(path.join(this_folder, 'NISPUF17.csv'))

pox_df = df.loc[:,['P_NUMVRC','SEX','HAD_CPOX']]
male_df = pox_df[pox_df['SEX'] == 1].dropna()
female_df = pox_df[pox_df['SEX'] == 2].dropna()

vacc_and_pox_male = male_df[(male_df['P_NUMVRC'].gt(0)) & (male_df['HAD_CPOX'] ==1)]
vacc_no_pox_male = male_df[(male_df['P_NUMVRC'].gt(0)) & (male_df['HAD_CPOX'] ==2)]

vacc_and_pox_female = female_df[(female_df['P_NUMVRC'].gt(0)) & (female_df['HAD_CPOX'] ==1)]
vacc_no_pox_female = female_df[(female_df['P_NUMVRC'].gt(0)) & (female_df['HAD_CPOX'] ==2)]

male_ratio = len(vacc_and_pox_male) / len(vacc_no_pox_male)
female_ratio = len(vacc_and_pox_female) / len(vacc_no_pox_female)

dict = {'male': male_ratio,
        'female': female_ratio}

print(dict)
