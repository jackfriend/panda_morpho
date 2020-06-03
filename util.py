import numpy as np
import pandas as pd
import seaborn as sns



def init_data(file_name=False, data_type="csv", style="white"):
    """
    Initiaize Numpy, Pandas, PyPlot, and Seaborn. Import data (csv by default)
    and export a dataframe.
    """
    sns.set() # initalize seaborn
    sns.set_style(style)

    # default case
    if data_type == "csv":
        df = pd.read_csv(file_name, na_values=['#VALUE!', '#DIV/0!'])
        return df
    #TODO: Add cases for non-csv file types
    else:
        print("ERROR: Currently only supports CSV format. \n > init_data(file_name=\"data.csv\")")
        pass
