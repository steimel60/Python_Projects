import pandas as pd
import numpy as np
from os import path


this_folder = path.dirname(__file__)
df = pd.read_csv(path.join(this_folder, 'NISPUF17.csv'))

flu_df = df.loc[:, ['CBF_01','P_NUMFLU']]
bf_flu = flu_df[flu_df['CBF_01'] == 1].dropna()
nbf_flu = flu_df[flu_df['CBF_01'] == 2].dropna()

breast_fed_total = len(bf_flu)
not_breast_fed_total = len(nbf_flu)

breast_fed_avg = np.sum(bf_flu['P_NUMFLU']) / breast_fed_total
not_avg = np.sum(nbf_flu['P_NUMFLU']) / not_breast_fed_total

tuple = (breast_fed_avg, not_avg)

print(tuple)
