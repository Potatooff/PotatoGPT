# LIBRARIES + CRATES IMPORTED 
from json import load as load_json
from pickle import dump, load
from numpy import array
from src.utils import preloader
from src.utils.useful import _error_text, _info_text
from src.utils.values import raw_data_path, trained_data_path

print(raw_data_path)
def _save_data(words, labels, training, output) -> None:
    """Save the trained data!"""

    _info_text("Saving trained data...")
    with open(trained_data_path, "wb") as f:
        dump((words, labels, training, output), f)
    _info_text("Saved trained data!")


def _load_data() -> None:
    """Responsible of loading the chatbot data."""

    global data
    try:
        _info_text("Loading raw data..")
        with open(raw_data_path) as file:
            data = load_json(file)
        _info_text("Loaded raw data!")

    except FileNotFoundError:
        _error_text("ERROR: data\intents.json is missing!")
        exit()


def _load_pretrained_data() -> None:
    """Responsible of loading the trained data for the chatbot."""

    global words, labels, training, output

    try:
        _info_text("Loading trained data...")
        with open(trained_data_path, "rb") as f:
            words, labels, training, output = load(f)
            holder = [words, labels, training, output]
        _info_text("Loaded trained data!")
        return holder

    except FileNotFoundError:
        _error_text("ERROR: data\\trained_data.pickle is missing!")
        exit()



def _train_data() -> None:
    """Responsible of training the chatbot data once loaded."""
    
    _info_text("Training raw data...")
    words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern = preloader._text_cleaner_v2(pattern)
            doc = preloader.nlp(pattern)
            wrds = [token.text.lower() for token in doc if not token.is_punct]
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])
            
        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        # Lemmatize the tokens using SpaCy
        wrds = [token.lemma_ for token in preloader.nlp(" ".join(doc)) if not token.is_punct]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = array(training)
    output = array(output)

    _info_text("Done training raw data, now saving...")
    _save_data(words, labels, training, output) # Save the trained data!



def _loader() -> None:
    """Responsible of loading the chatbot data and the trained data."""
        
    _load_data() # Load the data for the chatbot

    try:
        holder = _load_pretrained_data()  # Load trained data!
        holder.append(data)
        return holder

    # Build trained data!
    except:
        _train_data()
        _error_text("ERROR: Re-launch the bot again!")
        exit()

