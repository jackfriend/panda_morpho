import pandas as pd
import numpy
import scipy.stats as stats
from panda_extension import *
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

from panda_extension import *
import config


def clean_up(df, x=None, y=None, log=False):
    # clean up
    df = df[[x, y]]
    df = df.set_index([x, df.groupby(x).cumcount()])[y].unstack(0)

    if log:
        for col in df:
            df[col] = numpy.log(df[col])

    return df


def fstat_and_pvalue(*args):
    # let's calculate the F stat and P value. Drop N/A values, or f_oneway won't work
    mut_args = [] # *args gives us a tuple, we need to make a list
    for arg in args:
        mut_args.append(arg.dropna())

    fstat, pvalue = stats.f_oneway(*mut_args) # the * unpacks the list into seperate variables
    return fstat, pvalue


def get_anova(dataframe, x=None, y=None, categories=[]):
    # get_anova(df, x="dias_en_foam", y="total_length", categories=[0, 2, 4, 6])
    melt = pd.melt(dataframe.reset_index(),
            id_vars=['index'], # id_vars=['index'] mantains value pairings
            value_vars=categories)
    melt.columns = ['index', x, y]

    model = ols("{0} ~ {1}".format(y, x), data=melt).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table


if __name__ == "__main__":
    df = init_data(config.input_path)
    df = clean_up(df, x="dias_en_foam", y="total_length")
    fstat, pvalue = fstat_and_pvalue(df[2], df[4], df[6])
    anova = get_anova(df, x="dias_en_foam", y="total_length", categories=[0, 2, 4, 6])

    print(df)
    print("F statistic: {0}\nP value: {1}".format(fstat, pvalue))
    print(anova)
    print('\n')

    df = None # reset df

    df = init_data(config.input_path)
    df = clean_up(df, x="dias_en_foam", y="total_length", log=True)
    fstat, pvalue = fstat_and_pvalue(df[2], df[4], df[6])
    anova = get_anova(df, x="dias_en_foam", y="total_length", categories=[0, 2, 4, 6])

    print(df)
    print("F statistic: {0}\nP value: {1}".format(fstat, pvalue))
    print(anova)
