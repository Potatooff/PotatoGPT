from spacy import load as load_nlp
from src.utils.useful import _error_text, _info_text
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation


try:
    _info_text("Loading NLP model...")
    nlp = load_nlp("en_core_web_sm")   # Load Lemmatizer
    _info_text("NLP model loaded!")

except:
    _error_text("ERROR: An error loading the nlp en_core_web_sm!")
    exit()



def _text_cleaner_v2(text: str, punc: bool = True) -> str:

    """Clean the text from punctuation and stopwords!\n
    args:
        text: str - The text to clean
        punc: bool - Whether to remove punctuation or not\n
    returns: str - The cleaned text
    """

    text = text.lower()
    if punc:
        text = text.translate(str.maketrans("", "", punctuation)) # Remove every punctuation

    words: list = word_tokenize(text) # Tokenize the text for easier processing

    stop_words = set(stopwords.words('english')) # Get the list of English stopwords

    # Filter out the stopwords with a for loop
    filtered_words: list = [word for word in words if word.lower() not in stop_words]

    filtered_text: str = ' '.join(filtered_words) # Join the filtered words back into a sentence

    return filtered_text


def _download_nltk_stopwords() -> None:
    """Download the nltk stopwords!"""

    try:
        _info_text("Downloading nltk stopwords...")
        from nltk import download
        download('stopwords')
        _info_text("Downloaded nltk stopwords!")

    except:
        _error_text("ERROR: An error downloading the nltk stopwords!")
        exit()