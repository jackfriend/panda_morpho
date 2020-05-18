from panda_extension import *

df = init_data("aim_one.csv")

# comment out specific y axes not wanted
y_axes = [
        "total_length",
        "tail_length",
        "tail_musculate_width",
        "eye_width",
        "yolk_sac_width",
        "head_width",
        "tail_musculate_height",
        "tail_height",
        "yolk_sac_length",
        "yolk_to_mouth_length",
        "nose_length"
        ]

axis_info = {
        "total_length": ["Total Length", "Iterations of Foam Making", "Total Length"],
        "tail_length":["Tail Length", "Iterations of Foam Making", "Tail Length"] ,
        "tail_musculate_width": ["Tail Musculate Width", "Iterations of Foam Making", "Tail Musculate Width"],
        "eye_width": ["Eye Width", "Iterations of Foam Making", "Eye Width"],
        "yolk_sac_width": ["Yolk Sac Width", "Iterations of Foam Making", "Yolk Sac Width"],
        "head_width": ["Head Width", "Iterations of Foam Making", "Head Width"],
        "tail_musculate_height": ["Tail Musculate Width", "Iterations of Foam Making", "Tail Musculate Width"],
        "tail_height": ["Tail Height",  "Iterations of Foam Making", "Tail Height"],
        "yolk_sac_length": ["Yolk Sac Length", "Iterations of Foam Making", "Yolk Sac Length"],
        "yolk_to_mouth_length": ["Yolk to Mouth Length", "Iterations of Foam Making", "Yolk to Mouth Length"],
        "nose_length": ["Nose Length", "Iterations of Foam Making", "Nose Length"]  
        }

caption = """
    The immediate impact of iterations of foam nest constructions on tadpole morphometries. L. fragilis nests were collected and allowed to develop in their original, parentally produced foam until twelve days (x=0) in an ambient laboratory. The clutch of tadpoles recreated foam over two days (x=2), then morphometries were taken from each clutch. Foam was rinsed again so tadpoles could recreate foam for for the second time over two more days (x=4), and morphometries were taken again. Foam was rinsed a third time so tadpoles could recreate foam for the third time over two more days (x=6). 
"""

# for box plots
make_plot(df=df, x="dias_en_foam", y=y_axes, plotting_method=make_boxsubplot_by_trait, extra_info=axis_info, caption=caption)
# plt.tight_layout()
plt.draw()
plt.savefig(__file__ + ".jpg",
        dpi=None,
        quaility=None, # JPG quality; 1 <= x <= 95; None defaults to 95
        optimize=True, # optimizes JPEGs
        edgecolor='black',
        orientation='portrait'
        )
plt.close()
