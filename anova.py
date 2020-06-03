import pandas as pd
import numpy
import scipy.stats as stats
from panda_extension import *
import statsmodels.api as sm
from statsmodels.formula.api import ols

from panda_extension import *
import config


def clean_up(df, log=False):
    # clean up
    df = df[['total_length', 'dias_en_foam']]
    df = df.set_index(['dias_en_foam', df.groupby('dias_en_foam').cumcount()])['total_length'].unstack(0)
    # df = df.drop([2])

    if log:
        df[0] = numpy.log(df[0])
        df[2] = numpy.log(df[2])
        df[4] = numpy.log(df[4])
        df[6] = numpy.log(df[6])
    
    return df


def fstat_and_pvalue(df, *args):
    # let's calculate the F stat and P value. Drop N/A values, or f_oneway won't work
    fstat, pvalue = stats.f_oneway(args[0].dropna(), args[1].dropna(), args[2].dropna())
    return fstat, pvalue


def get_anova(dataframe):
    melt = pd.melt(dataframe.reset_index(),
            id_vars=['index'], # id_vars=['index'] mantains value pairings
            value_vars=[0, 2, 4, 6])
    melt.columns = ['index', 'dias_en_foam', 'total_length']

    model = ols("total_length ~ dias_en_foam", data=melt).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table








df = init_data(config.input_path)
df = clean_up(df)
fstat, pvalue = fstat_and_pvalue(df, df[2], df[4], df[6])
anova = get_anova(df)

print(df)
print("F statistic: {0}\nP value: {1}".format(fstat, pvalue))
print(anova)
print('\n')

df = None # reset df

df = init_data(config.input_path)
df = clean_up(df, log=True)
fstat, pvalue = fstat_and_pvalue(df, df[2], df[4], df[6])
anova = get_anova(df)

print(df)
print("F statistic: {0}\nP value: {1}".format(fstat, pvalue))
print(anova)


