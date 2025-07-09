
import os
import logging
from dotenv import load_dotenv

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Carga de variables de entorno
load_dotenv()

def obtener_ruta_archivo(nombre_archivo, carpeta='data/processed/'):
    """Devuelve la ruta completa a un archivo en carpeta dada"""
    base_path = os.getenv("BASE_DIR", os.getcwd())
    ruta = os.path.join(base_path, carpeta, nombre_archivo)
    logging.info(f"Ruta construida: {ruta}")
    return ruta

def log_etiqueta_sentimiento(texto, etiqueta):
    """Loguea una entrada analizada"""
    logging.info(f"Texto: '{texto[:50]}...' → Etiqueta: {etiqueta}")
