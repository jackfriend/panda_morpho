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


make_plot(df=df, x="dias_en_foam", y=y_axes, plotting_method=make_boxsubplot_by_trait, extra_info=axis_info)

plt.draw()
plt.savefig("figs.png", dpi=100)
# plt.show() # this needs to come after the plt.savefig()
plt.close()
