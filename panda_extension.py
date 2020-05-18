import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def help_me():
    """
    recap of functions below
    """
    print("""
    > init_data(file_name=\"data.csv\", data_type=\"csv\", style=\"any seaborn style\")
    \t Initalize Seaborn. 
    \t Import data from an external file and return it as a Panda Dataframe
    """)
    print("""
    > make_boxsubplot_by_trait(df=DataFrame, ax=axis-subplot, x=\"x-axis\", y=\"y-axis\", title=\"title\", xlabel=\"x axis label\", ylabel=\"y axis label\")
    \t Takes a Panda Dataframe that will be inputted into a subplot. Shows a box and whisker plot, with jitter, against a line graph of the increae.
    \t Optionally takes a title and replacement x-axis and y-axis labels
    """)

def init_data(file_name=False, data_type="csv", style="white"):
    """
    Initiaize Numpy, Pandas, PyPlot, and Seaborn. Import data (csv by default)
    and export a dataframe.
    """
    # sns.set() # initalize seaborn
    # sns.set_style(style)

    # default case
    if data_type == "csv":
        df = pd.read_csv('aim_one.csv', na_values=['#VALUE!', '#DIV/0!'])
        return df
    #TODO: Add cases for non-csv file types
    else:
        print("ERROR: Currently only supports CSV format. \n > init_data(file_name=\"data.csv\")")
        pass


def make_boxsubplot_by_trait(df=pd.DataFrame(), ax=False, x=False, y=False, title=False, xlabel=False, ylabel=False):
    """
    Makes a graph
    """
    # error handling
    if df.empty or not x or not y:
        print("ERROR: must input a dataframe, axis, x axis, and y axis.\n > make_graph(df=dataframe, ax=axis,  x=x_axis, y=y_axis)")

    else:

        title = title if title == False else "" 
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
        
        sns.boxplot(ax=ax, x=x , y=y, data=df)
        sns.swarmplot(ax=ax, x=x, y=y, data=df, color='k')
        sns.lineplot(ax=ax, x=x, y=y, data=mean_df, color='k', markers=True) 
        ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
        # plt.show()
        
        
def make_plot(df=pd.DataFrame(), x=False, y=[], plotting_method=False, extra_info={}):
    """
    Make a graph
    Take a list of y axis, specify the x axis, make sure to pass in the dataframe
    """

    # these variables determine the plot width and height
    num_of_plots = len(y)
    t_cols = 3
    t_rows = num_of_plots//t_cols + 1

    fig, ax = plt.subplots(nrows=t_rows, ncols=t_cols, figsize=(4*t_cols, 4*t_rows))
    # fig, ax = plt.subplots(nrows=t_rows, ncols=t_cols)

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


