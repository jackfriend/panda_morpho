library(tidyr)
library(dplyr)
library(gmodels)
library(crayon)
library(ggplot2)

# import data
source("config.r")
data <- read.csv(INPUT_PATH)
options(width=200)
sink(OUTPUT_PCA_PATH, append=FALSE, split=TRUE)
pdf(OUTPUT_PCA_PDF) # We will export plots to this PDF


# organize the data
data <- data %>%
    select(dias_en_foam, clutch, total_length, tail_length, tail_musculate_width, eye_width, head_width, tail_musculate_height, tail_height, yolk_sac_length, yolk_to_mouth_length, nose_length)

data$dias_en_foam <- factor(data$dias_en_foam) # change dias_en_foam to categorical
data$clutch <- factor(data$clutch) # change dias_en_foam to categorical


# Do the PCA
pr_data <- data %>%
    select(- c(dias_en_foam, clutch)) # drop dias_en_foam for pr

pr <- prcomp(na.omit(pr_data), scale=TRUE)

# extract PC scores and add to data
data <- merge(data, pr$x, by="row.names", all.x=TRUE)
data <- data[order(as.numeric(data$Row.names)), ] # put the data in ascending order
data <- data %>%
    select(- c(Row.names)) # drop Row.names column now
row.names(data) <- NULL # reset indexing

# print an output
print(data)

# Plot
plot(pr, type='l')
biplot(pr, scale=0)
ggplot(data, aes(PC1, PC2, col=dias_en_foam, fill=dias_en_foam)) +
   stat_ellipse(geom = "polygon", col="black", alpha=0.5) +
   geom_point(shape=21, col="black")

#ANOVA of PCA
anova_data <- data %>%
    select(clutch, dias_en_foam, PC4) %>% # Change the PC to the PC we want to use
    group_by(dias_en_foam)

summary <- anova_data %>%
    summarize(PC4.mean = mean(PC4, na.rm=TRUE),
              PC4.sd = sd(PC4, na.rm=TRUE),
              PC4.N = length(PC4),
              PC4.se = PC4.sd/sqrt(PC4.N),
              PC4.95_lower = ci(PC4, na.rm=TRUE)[2],
              PC4.95_upper = ci(PC4, na.rm=TRUE)[3],
              PC4.min = min(PC4, na.rm=TRUE),
              PC4.max = max(PC4, na.rm=TRUE))

print("___________________________________________________________________________")
print("SUMMARY:")
print(summary)

linear_model <- lm(PC4 ~ dias_en_foam, data=anova_data)
log_linear_model <- lm(log(PC4) ~ dias_en_foam, data=anova_data)
anova_lm <- anova(linear_model)
log_anova_lm <- anova(log_linear_model)

print("___________________________________________________________________________")
print("ANOVA MODEL:")
print(summary(linear_model))
print(anova_lm)

print("___________________________________________________________________________")
print("LOG ANOVA MODEL:")
print(summary(log_linear_model))
print(log_anova_lm)




# Output data to file
dev.off()
