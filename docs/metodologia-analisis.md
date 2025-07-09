
# 🧠 Metodología de Análisis de Sentimiento

Este documento describe la lógica y técnicas aplicadas para clasificar el sentimiento en comentarios de clientes.

## 📚 Técnicas Aplicadas
- **NLTK / VADER**: modelo basado en léxico para polaridad simple.
- **spaCy**: procesamiento avanzado (lemas, entidades) con reglas heurísticas iniciales.
- **scikit-learn** (opcional): posible integración de modelo entrenado con feedback clasificado.

## ⚖️ Clasificación de Sentimiento
- Positivo: expresiones de gratitud, satisfacción, eficiencia
- Negativo: reclamos, demora, fallos en el producto
- Neutral: expresiones ambiguas o mixtas

## 🧪 Evaluación
- Validación cruzada manual entre NLTK y spaCy
- Posibilidad de integrar feedback humano para fine-tuning

## 🔍 Consideraciones Éticas
- Datos anonimizados
- Uso responsable del feedback para mejoras concretas
