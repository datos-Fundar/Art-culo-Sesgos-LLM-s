# Levando dataset de distacias LAPOP

lpop_distances <- read.csv('./outputs/lpop_distances.csv')


#q2 edad
#q1tb sexo
#ur1new domicilio
#edr educacion
#conocim politizacion
#q10newt ingresos



## GPT ----

lmodel_gpt <- lm((gpt_distance_norm) ~ q2 + q1tb + ur1new + edr + conocim   , data = lpop_distances)
summary(lmodel_gpt)
predicted_values_gpt <- predict(lmodel_gpt)
residuals_gpt <- residuals(lmodel_gpt)

### Crear un gráfico de residuos vs. valores predichos
plot(predicted_values_gpt, residuals_gpt,
     xlab = "Valores Predichos", ylab = "Residuos",
     main = "Gráfico de Residuos vs Valores Predichos - GPT")
abline(h = 0, lty = 2)

## Cohere ----
lmodel_cohere <- lm((cohere_distance_norm) ~ q2 + q1tb +  ur1new + edr + conocim , data = lpop_distances)
summary(lmodel_cohere)
predicted_values_cohere <- predict(lmodel_cohere)
residuals_cohere <- residuals(lmodel_cohere)

### Crear un gráfico de residuos vs. valores predichos
plot(predicted_values_cohere, residuals_cohere, 
     xlab = "Valores Predichos", ylab = "Residuos",
     main = "Gráfico de Residuos vs Valores Predichos - Cohere")
abline(h = 0, lty = 2)

## Bard ----

lmodel_bard <- lm((bard_distance_norm) ~ q2 + q1tb +  ur1new + edr + conocim , data = lpop_distances)
summary(lmodel_bard)
predicted_values_bard <- predict(lmodel_bard)
residuals_bard <- residuals(lmodel_bard)

### Crear un gráfico de residuos vs. valores predichos
plot(predicted_values_bard, residuals_bard, 
     xlab = "Valores Predichos", ylab = "Residuos", 
     main = "Gráfico de Residuos vs Valores Predichos - Bard")
abline(h = 0, lty = 2)

