library(dplyr)
library(crayon)

# import data
source("config.r")
data <- read.csv(INPUT_PATH)
data <- data %>%
    select(total_length, tail_length, tail_musculate_width, eye_width, head_width, tail_musculate_height, tail_height, yolk_sac_length, yolk_to_mouth_length, nose_length)

print(data)
pr <- prcomp(na.omit(data))

print(pr)
