import pandas as pd
import scipy.stats as stats
from panda_extension import *
import config

df = init_data(config.input_path)

df = df[['total_length', 'dias_en_foam']]
df = df.groupby('dias_en_foam')
# df = df.transpose()

print(df.head())
