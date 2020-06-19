library(gmodels)
library(dplyr)
library(crayon)

# import data
source("config.r")
data <- read.csv(INPUT_PATH)

# output data to file
options(width=300)
sink(OUTPUT_PATH, append=FALSE, split=TRUE)

# Organize the data -> group by dias_en_foam
total_length_data <- data %>%
    select(clutch, dias_en_foam, total_length) %>%
    group_by(dias_en_foam)

# turn the dias_en_foam column from continuous to discrete
total_length_data$dias_en_foam <- factor(total_length_data$dias_en_foam)

# >>>
# summary of the mean, SD, and N values
total_length_summary <- total_length_data %>%
    summarize(total_length.mean = mean(total_length, na.rm=TRUE),
              total_length.sd = sd(total_length, na.rm=TRUE),
              total_length.N = length(total_length),
              total_length.se = total_length.sd/sqrt(total_length.N),
              total_length.95_lower = ci(total_length, na.rm=TRUE)[2],
              total_length.95_upper = ci(total_length, na.rm=TRUE)[3],
              total_length.min = min(total_length, na.rm=TRUE),
              total_length.max = max(total_length, na.rm=TRUE))
cat(green("────────────────────────────────────────────────────────────────────────────────────\n"))
print("SUMMARY:")
print(total_length_summary)
# <<<

# the anova model
# (Response ~ predictor, data=DataFrame)
linear_model <- lm(total_length ~ dias_en_foam, data=total_length_data)
log_linear_model <- lm(log(total_length) ~ dias_en_foam, data=total_length_data)
# run Anova
anova_lm <- anova(linear_model)
log_anova_lm <- anova(log_linear_model)

cat(green("────────────────────────────────────────────────────────────────────────────────────\n"))
print("ANOVA MODEL:")
print(summary(linear_model))
print(anova_lm)

png(OUTPUT_PNG, units="px", width=900, height=900)
par(mfrow=c(2,2))
plot(linear_model)
dev.off()

cat(green("────────────────────────────────────────────────────────────────────────────────────\n"))
print("LOG ANOVA MODEL:")
print(summary(log_linear_model))
print(log_anova_lm)
