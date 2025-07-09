
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
import pandas as pd

# NLTK: VADER funciona mejor con inglés, pero ilustramos estructura
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# spaCy model for Spanish already loaded in nlp_pipeline.py

def sentimiento_nltk(texto):
    """Clasifica sentimiento usando VADER (demo con textos limpios)"""
    score = sia.polarity_scores(texto)
    if score['compound'] >= 0.05:
        return 'Positivo'
    elif score['compound'] <= -0.05:
        return 'Negativo'
    else:
        return 'Neutral'

def sentimiento_spacy(texto):
    """Placeholder para clasificador spaCy o Regla manual"""
    # Aquí podés integrar un clasificador entrenado o heurística custom
    if 'excelente' in texto or 'muy bueno' in texto:
        return 'Positivo'
    elif 'malo' in texto or 'deficiente' in texto:
        return 'Negativo'
    else:
        return 'Neutral'
