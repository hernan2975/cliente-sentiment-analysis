
import nltk
import spacy

nltk.download('punkt')
nltk.download('stopwords')

nlp_spacy = spacy.load("es_core_news_sm")

def nltk_tokenize(texto):
    """Tokeniza texto usando NLTK"""
    from nltk.tokenize import word_tokenize
    return word_tokenize(texto)

def spacy_pipeline(texto):
    """Procesa texto con spaCy: lematiza y detecta entidades"""
    doc = nlp_spacy(texto)
    lemas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    return {"lemas": lemas, "entidades": entidades}
