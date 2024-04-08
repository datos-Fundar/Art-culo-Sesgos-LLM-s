# Levando dataset de distacias LATIN

latin_distances <- read.csv('./outputs/latin_distances.csv')


#p46stgbs politizado
# s13 irse del pais
#p18st ideologia
#s16 estudios
#s17 estudios padres


## GPT ----

lmodel_gpt <- lm((gpt_distance_norm) ~ edad+sexo+ p18st +s16+s13+s17+p46stgbs , data = latin_distances)
summary(lmodel_gpt)
predicted_values_gpt <- predict(lmodel_gpt)
residuals_gpt <- residuals(lmodel_gpt)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values_gpt, residuals_gpt,
     xlab = "Valores Predichos", ylab = "Residuos", 
     main = "Gráfico de Residuos vs Valores Predichos GPT")
abline(h = 0, lty = 2)

## Cohere ----

lmodel_cohere <- lm((cohere_distance_norm) ~ edad+sexo+ p18st +s16+s13+s17+p46stgbs , data = latin_distances)
summary(lmodel_cohere)
predicted_values_cohere <- predict(lmodel_cohere)
residuals_cohere <- residuals(lmodel_cohere)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values_cohere, residuals_cohere, 
     xlab = "Valores Predichos", ylab = "Residuos",
     main = "Gráfico de Residuos vs Valores Predichos Cohere")
abline(h = 0, lty = 2)


## Bard ----

lmodel_bard <- lm((bard_distance_norm) ~ edad+sexo+ p18st +s16+s13+s17+p46stgbs , data = latin_distances)
summary(lmodel_bard)
predicted_values_bard <- predict(lmodel_bard)
residuals_bard <- residuals(lmodel_bard)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values_bard, residuals_bard, 
     xlab = "Valores Predichos", ylab = "Residuos", 
     main = "Gráfico de Residuos vs Valores Predichos Bard")
abline(h = 0, lty = 2)

