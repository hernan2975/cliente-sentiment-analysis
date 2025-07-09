import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('spanish'))

def limpiar_texto(texto):
    """Limpia texto eliminando símbolos, espacios y stopwords"""
    texto = re.sub(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', texto)
    texto = texto.lower().strip()
    tokens = texto.split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    return ' '.join(tokens)

def transformar_dataframe(df, columna_texto='comentario'):
    """Aplica limpieza a columna de texto"""
    df['texto_limpio'] = df[columna_texto].apply(limpiar_texto)
    return df

