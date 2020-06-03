import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from graph import *
from anova import *
from util import *
import config



if __name__ == "__main__":
    # init
    df = init_data(config.INPUT_PATH)
    x = "dias_en_foam"
    y = "total_length"

    # make the graph
    fig, (ax1, ax2) = plt.subplots(1, 2)
    plot = make_boxsubplot_by_trait(df,
        ax=ax1,
        x=x,
        y=y)
    
    df = None
    df = init_data(config.INPUT_PATH)
    df = clean_up(df, x=x, y=y, log=True)
    df[2] = reject_outlier(df[2])
    df[2] = reject_outlier(df[2])
    df[6] = reject_outlier(df[6])

    sns.boxplot(ax=ax2, x=x , y="value", data=pd.melt(df), color="white")
    sns.swarmplot(ax=ax2, x=x , y="value", data=pd.melt(df), color="k")

    fstat, pvalue = fstat_and_pvalue(df[2], df[4], df[6])
    anova = get_anova(df, x=x, y=y, categories=[0, 2, 4, 6])

    print(df)
    print("F statistic: {0}\nP value: {1}".format(fstat, pvalue))
    print(anova)

    plt.draw()
    plt.savefig(config.OUTPUT_PATHS['total_length'],
            dpi=None,
            quaility=None, # JPG quality; 1 <= x <= 95; None defaults to 95
            optimize=True, # optimizes JPEGs
            edgecolor='black',
            orientation='portrait'
            )
    plt.close()
    

