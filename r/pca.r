library(tidyr)
library(dplyr)
library(crayon)
library(ggplot2)

# import data
source("config.r")
data <- read.csv(INPUT_PATH)
sink(OUTPUT_PCA_PATH, append=FALSE, split=TRUE)
pdf(OUTPUT_PCA_PDF) # We will export plots to this PDF


# organize the data
data <- data %>%
    select(dias_en_foam, total_length, tail_length, tail_musculate_width, eye_width, head_width, tail_musculate_height, tail_height, yolk_sac_length, yolk_to_mouth_length, nose_length)

data$dias_en_foam <- factor(data$dias_en_foam) # change dias_en_foam to categorical


# Do the PCA
pr_data <- data %>%
    select(- c(dias_en_foam)) # drop dias_en_foam for pr

pr <- prcomp(na.omit(pr_data), scale=TRUE)

# extract PC scores and add to data
data <- merge(data, pr$x, by="row.names", all.x=TRUE)
data <- data[order(as.numeric(data$Row.names)), ] # put the data in ascending order
    
print(head(data))


# Plot
plot(pr, type='l')
biplot(pr, scale=0)
ggplot(data, aes(PC1, PC2, col=dias_en_foam, fill=dias_en_foam)) +
   stat_ellipse(geom = "polygon", col="black", alpha=0.5) +
   geom_point(shape=21, col="black")


# Output data to file
dev.off()
