from spacy import load as load_nlp
from src.utils.useful import _error_text


try:
    nlp = load_nlp("en_core_web_sm")   # Load Lemmatizer
except:
    _error_text("ERROR: An error loading the nlp en_core_web_sm!")
    exit()