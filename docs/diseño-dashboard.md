
# 🧭 Diseño del Dashboard de Satisfacción de Cliente

Este dashboard tiene como objetivo visualizar el sentimiento de los clientes a partir de sus comentarios y reseñas. Provee métricas clave para la toma de decisiones en áreas como atención al cliente, ventas y posventa.

## 🔍 Indicadores Principales
- Distribución de sentimientos (Positivo / Negativo / Neutral)
- Nube de palabras clave en comentarios
- Tendencia temporal de satisfacción
- Filtros por canal de origen (formulario, redes, correo)

## 🗺️ Mapa de Calor
Representa satisfacción por punto de contacto, con colores que indican intensidad del sentimiento.

## 🔄 Interactividad
- Segmentaciones por fecha, canal y producto
- Tooltip con comentario original
- Filtros dinámicos para comparar periodos

## 📂 Fuentes de Datos
- `sentimiento_nltk.csv`
- `sentimiento_spacy.csv`
- Datos crudos desde `data/raw/`

## 💡 Recomendaciones
- Actualizar el dashboard cada semana
- Exportar KPIs para informes ejecutivos
