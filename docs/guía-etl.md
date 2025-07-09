
# 🔧 Guía del Pipeline ETL

Este módulo transforma comentarios de clientes en datos estructurados listos para análisis de sentimiento.

## 🧩 Flujo General
1. Extracción (`extract.py`)
   - Formatos soportados: `.csv`, `.json`, `.txt`
   - Orígenes: encuestas, redes sociales, correos

2. Transformación (`transform.py`)
   - Limpieza de texto
   - Tokenización y stopwords
   - Normalización con `pandas`

3. Carga (`load.py`)
   - Exportación a `.csv`
   - Compatibilidad con Power BI

## 🔐 Buenas Prácticas
- No modificar `data/raw/`
- Validar fecha y texto antes de tokenizar
- Manejar rutas dinámicas con `dotenv`

## 🚀 Automatización
Se puede agendar este pipeline con `cron`, `Airflow` o flujos de Power BI.
