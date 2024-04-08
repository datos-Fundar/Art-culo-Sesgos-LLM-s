# GPT


latin_distances$p18st[latin_distances$p18st == 97] <- NA #Reemplazo "Ninguna" en ideo por NA
latin_distances$p18st[latin_distances$p18st == -1] <- NA #Reemplazo "No sabe" en ideo por NA
latin_distances$p18st[latin_distances$p18st == -2] <- NA #Reemplazo "No contesta" en ideo por NA
latin_distances$p46stgbs[latin_distances$p46stgbs == -1] <- NA  #Reemplazo "No sabe" en interes politica por NA
latin_distances$p46stgbs[latin_distances$p46stgbs == -2] <- NA #Reemplazo "No contesta" en interes politica por NA
latin_distances$s13[latin_distances$s13 == -5] <- NA #Reemplazo "'No sabe / No contesta'" en irse del pais por NA

#p46stgbs politizado
# s13 irse del pais
#p18st ideologia
#s16 estudios
#s17 estudios padres

# latin_distances <- read.csv('./outputs/latin_distances.csv')

lmodel <- lm((gpt_distance_norm) ~ edad+sexo+ p18st +s16+s13+s17+p46stgbs , data = latin_distances)
summary(lmodel)
predicted_values <- predict(lmodel)
residuals <- residuals(lmodel)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos GPT")
abline(h = 0, lty = 2)

# Cohere

lmodel <- lm((cohere_distance_norm) ~ edad+sexo+ p18st +s16+s13+s17+p46stgbs , data = latin_distances)
summary(lmodel)
predicted_values <- predict(lmodel)
residuals <- residuals(lmodel)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos GPT")
abline(h = 0, lty = 2)


# Bard

lmodel <- lm((bard_distance_norm) ~ edad+sexo+ p18st +s16+s13+s17+p46stgbs , data = latin_distances)
summary(lmodel)
predicted_values <- predict(lmodel)
residuals <- residuals(lmodel)

# Crear un gráfico de residuos vs. valores predichos
plot(predicted_values, residuals, xlab = "Valores Predichos", ylab = "Residuos", main = "Gráfico de Residuos vs Valores Predichos GPT")
abline(h = 0, lty = 2)
