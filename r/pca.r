library(dplyr)
library(crayon)

# import data
source("config.r")
data <- read.csv(INPUT_PATH)

# Output data to file
options(width=300)
sink(OUTPUT_PCA, append=FALSE, split=TRUE)
png(OUTPUT_PCA_PNG, units="px", width=900, height=900)
par(mfrow=c(2,2))

# organize the data
data <- data %>%
    select(total_length, tail_length, tail_musculate_width, eye_width, head_width, tail_musculate_height, tail_height, yolk_sac_length, yolk_to_mouth_length, nose_length)

# PCA init, scale=TRUE will set the mean to 0
pr <- prcomp(na.omit(data), scale=TRUE)


print(pr)
dev.off()
