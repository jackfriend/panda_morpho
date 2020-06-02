import pandas as pd
import scipy.stats as stats
from panda_extension import *
import config

# for the ANOVA table 
import statsmodels.api as sm
from statsmodels.formula.api import ols

# init
df = init_data(config.input_path)

# clean up
df = df[['total_length', 'dias_en_foam']]
df = df.set_index(['dias_en_foam', df.groupby('dias_en_foam').cumcount()])['total_length'].unstack(0)
# df = df.drop([2])
print(df)

# let's calculate the F stat and P value. Drop N/A values, or f_oneway won't work
fstat, pvalue = stats.f_oneway(
#       df[0].dropna(),
       df[2].dropna(),
       df[4].dropna(),
       df[6].dropna()
       )

print("F statistic: {0}\nP value: {1}".format(fstat, pvalue))


# ANOVA
df = df.drop([0])
melt = pd.melt(df.reset_index(),
        id_vars=['index'], # id_vars=['index'] mantains value pairings
        value_vars=[0, 2, 4, 6])
melt.columns = ['index', 'dias_en_foam', 'total_length']

model = ols("total_length ~ dias_en_foam", data=melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
