# LIBRARIES + CRATES IMPORTED 
from json import load as load_json
from pickle import dump, load
from numpy import array
from src.utils.preloader import nlp
from src.utils.useful import _error_text


def _save_data(words, labels, training, output) -> None:
    """Save the trained data!"""

    with open(r"data\trained_data.pickle", "wb") as f:
        dump((words, labels, training, output), f)


def _load_data() -> None:
    """Responsible of loading the chatbot data."""

    global data
    try:
        with open(r"data\intents.json") as file:
            data = load_json(file)

    except FileNotFoundError:
        _error_text("ERROR: intents.json is missing!")
        exit()


def _load_pretrained_data() -> None:
    """Responsible of loading the trained data for the chatbot."""

    global words, labels, training, output

    try:
        with open(r"data\trained_data.pickle", "rb") as f:
            words, labels, training, output = load(f)
            holder = [words, labels, training, output]
            return holder

    except FileNotFoundError:
        _error_text("ERROR: trained_data.pickle is missing!")
        exit()



def _train_data() -> None:
    """Responsible of training the chatbot data once loaded."""
    
    words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            doc = nlp(pattern)
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
        wrds = [token.lemma_ for token in nlp(" ".join(doc)) if not token.is_punct]

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

