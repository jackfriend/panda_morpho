import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import config
from util import *



def make_boxsubplot_by_trait(df=pd.DataFrame(),
        ax=False,
        x=False,
        y=False,
        title=False,
        mean=False,
        xlabel=False,
        ylabel=False):
    """
    Makes a graph
    """
    # error handling
    if df.empty or not x or not y:
        print("ERROR: must input a dataframe, axis, x axis, and y axis.\n > make_graph(df=dataframe, ax=axis,  x=x_axis, y=y_axis)")

    else:

        title = ""  if title == False else title
        xlabel = x if xlabel == False else xlabel
        ylabel = y if ylabel == False else ylabel

        # make dataframe for total lengths
        mean_df={x: [0, 1, 2, 3],
                y: [
                        df.loc[df[x] == 0, y].mean(),
                        df.loc[df[x] == 2, y].mean(),
                        df.loc[df[x] == 4, y].mean(),
                        df.loc[df[x] == 6, y].mean(),
                ]}

        mean_df = pd.DataFrame(data=mean_df)

        # use Seaborn to make plots
        sns.boxplot(ax=ax, x=x , y=y, data=df, color="white")
        sns.swarmplot(ax=ax, x=x, y=y, data=df, color='k')

        if mean:
            sns.lineplot(ax=ax, x=x, y=y, data=mean_df, color='k', markers=True)

        ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
        # plt.show()


def make_plot(df=pd.DataFrame(), x=False, y=[], plotting_method=False, extra_info={}, caption=False, plotsize_factor=4):
    """
    Make a graph
    Take a list of y axis, specify the x axis, make sure to pass in the dataframe
    """

    # these variables determine the plot width and height
    num_of_plots = len(y)
    t_cols = 3
    t_rows = num_of_plots//t_cols + 1

    fig, ax = plt.subplots(nrows=t_rows, ncols=t_cols, figsize=(plotsize_factor*t_cols, plotsize_factor*t_rows))
    plt.subplots_adjust(hspace=0.5, wspace=0.5)

    # for caption
    caption = ""  if caption == False else caption
    fig.suptitle(caption, y=0.05, fontsize=10, wrap=True)

    for i, el in enumerate(y, start=0):
        # determines the positions of the enumerated subplot
        row = i//t_cols
        col = i % t_cols

        plotting_method(df=df,
                ax=ax[row][col],
                x=x,
                y=el,
                title=extra_info[el][0],
                xlabel=extra_info[el][1],
                ylabel=extra_info[el][2])



if __name__ =="__main__":
    df = init_data(config.INPUT_PATH)

    # for box plots
    make_plot(df=df,
        x="dias_en_foam",
        y=config.y_axes,
        plotting_method=make_boxsubplot_by_trait,
        extra_info=config.axis_info,
        caption=config.caption)
    # plt.tight_layout()
    plt.draw()
    plt.savefig(config.OUTPUT_PATHS['aim_one'],
            dpi=None,
            quaility=None, # JPG quality; 1 <= x <= 95; None defaults to 95
            optimize=True, # optimizes JPEGs
            edgecolor='black',
            orientation='portrait'
            )
    plt.close()
