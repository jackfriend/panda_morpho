library(dplyr)
library(crayon)

# import data
source("config.r")
data <- read.csv(INPUT_PATH)

# Organize the data -> group by dias_en_foam
total_length_data <- data %>%
    select(clutch, dias_en_foam, total_length) %>%
    group_by(dias_en_foam)

# just a summary of the mean, SD, and N values
total_length_summary <- total_length_data %>%
    summarize(total_length.mean = mean(total_length, na.rm=TRUE),
              total_length.sd = sd(total_length, na.rm=TRUE),
              total_length.N = length(total_length))
cat(green("────────────────────────────────────────────────────────────────────────────────────\n"))
print("SUMMARY:")
print(total_length_summary)

# the anova model
# (Response ~ predictor, data=DataFrame)
linear_model <- lm(total_length ~ dias_en_foam, data=total_length_data)
log_linear_model <- lm(log(total_length) ~ dias_en_foam, data=total_length_data)

cat(green("────────────────────────────────────────────────────────────────────────────────────\n"))
print("ANOVA MODEL:")
print(summary(linear_model))

cat(green("────────────────────────────────────────────────────────────────────────────────────\n"))
print("LOG ANOVA MODEL:")
print(summary(log_linear_model))
