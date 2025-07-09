
import pandas as pd
from pathlib import Path

def exportar_csv(df, path):
    """Exporta DataFrame a CSV"""
    try:
        df.to_csv(path, index=False, encoding='utf-8')
        print(f"[INFO] Exportado a: {path}")
    except Exception as e:
        print(f"[ERROR] Exportación fallida: {e}")
