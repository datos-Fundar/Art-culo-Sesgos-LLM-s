
#q2 edad
#q1tb sexo
#ur1new domicilio
#edr educacion
#conocim politizacion
#q10newt ingresos

# GPT

# lpop_distances <- read.csv('./outputs/lpop_distances.csv')

lmodel <- lm((gpt_distance_norm) ~ q2 + q1tb + ur1new + edr + conocim   , data = lpop_distances)
summary(lmodel)
predicted_values <- predict(lmodel)
residuals <- residuals(lmodel)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos GPT")
abline(h = 0, lty = 2)

# Cohere
lmodel <- lm((cohere_distance_norm) ~ q2 + q1tb +  ur1new + edr + conocim , data = lpop_distances)
summary(lmodel)
predicted_values <- predict(lmodel)
residuals <- residuals(lmodel)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos")
abline(h = 0, lty = 2)

# Bard

lmodel <- lm((bard_distance_norm) ~ q2 + q1tb +  ur1new + edr + conocim , data = lpop_distances)
summary(lmodel)
predicted_values <- predict(lmodel)
residuals <- residuals(lmodel)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos")
abline(h = 0, lty = 2)