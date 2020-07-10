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
get_anova_of_pca <- function(dataset, PC_comp, PC_comp_str) {

    anova_data <- dataset %>%
        select(clutch, dias_en_foam, {{PC_comp}}) %>% # Change the PC to the PC we want to use
        group_by(dias_en_foam)

    summary <- anova_data %>%
        summarize(
                  N        := length( {{PC_comp}}),
                  mean     := mean( {{PC_comp}}, na.rm=TRUE),
                  sd       := sd( {{PC_comp}},  na.rm=TRUE),
                  se       := ( sd / sqrt( N )),
                  lower    := ci( {{PC_comp}} , na.rm=TRUE)[2],
                  upper    := ci( {{PC_comp}} , na.rm=TRUE)[3],
                  min      := min( {{PC_comp}} , na.rm=TRUE),
                  max      := max( {{PC_comp}} , na.rm=TRUE)
                  )

    print("___________________________________________________________________________")
    print("SUMMARY:")
    print(summary)
    print(anova_data)

    # linear model
    lm_formula <- paste(PC_comp_str, "~ dias_en_foam")
    linear_model <- lm(lm_formula, data=anova_data)
    # Log linear model
    log_lm_formula <- paste("log(", PC_comp_str, ") ~ dias_en_foam")
    log_linear_model <- lm(log_lm_formula, data=anova_data)
    # ANOVA
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
}

print("")
print("")
print("___________________________________________________________________________")
print("PC1:")
get_anova_of_pca(data, PC1, "PC1")
print("")
print("")
print("___________________________________________________________________________")
print("PC2:")
get_anova_of_pca(data, PC2, "PC2")
print("")
print("")
print("___________________________________________________________________________")
print("PC3:")
get_anova_of_pca(data, PC3, "PC3")
print("___________________________________________________________________________")
print("")
print("")
print("PC4:")
get_anova_of_pca(data, PC4, "PC4")

# Output data to file
dev.off()
