from panda_extension import *
from config import input_path, output_path

df = init_data(input_path)

# for box plots
make_plot(df=df, x="dias_en_foam", y=y_axes, plotting_method=make_boxsubplot_by_trait, extra_info=axis_info, caption=caption)
# plt.tight_layout()
plt.draw()
plt.savefig(output_path,
        dpi=None,
        quaility=None, # JPG quality; 1 <= x <= 95; None defaults to 95
        optimize=True, # optimizes JPEGs
        edgecolor='black',
        orientation='portrait'
        )
plt.close()
