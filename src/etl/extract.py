import pandas as pd
from pathlib import Path

def load_csv(path):
    """Carga un archivo CSV en un DataFrame"""
    try:
        df = pd.read_csv(path, encoding='utf-8')
        print(f"[INFO] Cargado: {path}")
        return df
    except Exception as e:
        print(f"[ERROR] No se pudo cargar {path}: {e}")
        return pd.DataFrame()

def load_txt(path):
    """Carga un archivo de texto plano como lista"""
    try:
        with open(path, "r", encoding='utf-8') as file:
            lines = file.readlines()
        print(f"[INFO] Cargado: {path}")
        return lines
    except Exception as e:
        print(f"[ERROR] No se pudo cargar {path}: {e}")
        return []
