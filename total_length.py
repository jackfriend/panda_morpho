import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from graph import *
from util import *
import config



if __name__ == "__main__":
    # init
    df = init_data(config.INPUT_PATH)

    # make the graph
    fig, ax = plt.subplots()
    plot = make_boxsubplot_by_trait(df,
        ax=ax,
        x="dias_en_foam",
        y="total_length")
    plt.draw()
    plt.savefig(config.OUTPUT_PATHS['total_length'],
            dpi=None,
            quaility=None, # JPG quality; 1 <= x <= 95; None defaults to 95
            optimize=True, # optimizes JPEGs
            edgecolor='black',
            orientation='portrait'
            )
    plt.close()
