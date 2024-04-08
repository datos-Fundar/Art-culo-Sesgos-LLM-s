
#q2 edad
#q1tb sexo
#ur1new domicilio
#edr educacion
#conocim politizacion
#q10newt ingresos

# Levando dataset de distacias

lpop_distances <- read.csv('./outputs/lpop_distances.csv')

## GPT ----

lmodel_gpt <- lm((gpt_distance_norm) ~ q2 + q1tb + ur1new + edr + conocim   , data = lpop_distances)
summary(lmodel_gpt)
predicted_values <- predict(lmodel_gpt)
residuals <- residuals(lmodel_gpt)

### Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos GPT")
abline(h = 0, lty = 2)

## Cohere ----
lmodel_cohere <- lm((cohere_distance_norm) ~ q2 + q1tb +  ur1new + edr + conocim , data = lpop_distances)
summary(lmodel_cohere)
predicted_values <- predict(lmodel_cohere)
residuals <- residuals(lmodel_cohere)

### Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos")
abline(h = 0, lty = 2)

## Bard ----

lmodel_bard <- lm((bard_distance_norm) ~ q2 + q1tb +  ur1new + edr + conocim , data = lpop_distances)
summary(lmodel_bard)
predicted_values <- predict(lmodel_bard)
residuals <- residuals(lmodel_bard)

### Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos")
abline(h = 0, lty = 2)

