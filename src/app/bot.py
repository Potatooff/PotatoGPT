# Modules
from src.utils.training import _loader
from time import sleep
from string import punctuation
from random import choice as randomizer
from numpy import argmax, array
from fuzzywuzzy.fuzz import token_set_ratio
from keras.models import Sequential
from tensorflow import keras
from src.utils.preloader import nlp




words, labels, training, output, data = _loader() # DATA LOADER

"""lost words"""
idk = [
    "Sorry, i did not understand",
    "Sorry i didn't get it",
    "Please could you rephrase it",
    "Please be more clear",
    "Please i am still in training",
    "Sorry i have no idea of what you just said",
    "My bad, i am not that advanced"
]


def _fuzzy_bag_of_words(s, words):
    """bag of words"""

    bag = [0 for _ in range(len(words))]

    # Tokenize and lemmatize the input string using SpaCy
    s_doc = nlp(s)
    s_words = [token.lemma_ for token in s_doc if not token.is_punct]

    for se in s_words:
        for i, w in enumerate(words):
            if token_set_ratio(w, se) >= 70:
                bag[i] = 1

    return array(bag)


def _typing_effect(text):
    """ Typing effects"""

    for char in text:
        print(char, end="", flush=True)
        sleep(0.05)
    print("\n")


def _clean_text(text):
    """Remove punctuation"""

    corrected = text.lower()
    cleaned_text = corrected.translate(str.maketrans("", "", punctuation))
    return cleaned_text


model = Sequential() # Defining model
def train_ai(save:bool = False):

    # Input Layer
    model.add(keras.layers.InputLayer(input_shape=(None, len(training[0]))))

    # First Layer
    model.add(keras.layers.Dense(
        units=512,
        activation='relu',
        use_bias=True   
    ))

    model.add(keras.layers.Dense(
        units=512,
        activation='relu',
        use_bias=True   
    ))

    model.add(keras.layers.Dense(
        units=256,
        activation='relu',
        use_bias=True 
    ))

    model.add(keras.layers.Dense(
        units=128,
        activation='relu',
        use_bias=True   
    ))

    model.add(keras.layers.Dense(
        units=64,
        activation='relu',
        use_bias=True
    ))

    model.add(keras.layers.Dense(
        units=32,
        activation='relu',
        use_bias=True
    ))

    model.add(keras.layers.Dense(
        units=len(output[0]),
        activation='softmax',
        use_bias=True
    )    
    )

    # Dropout regularization
    #model.add(keras.layers.Dropout(0.5))

    # Compile the model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy'])

    # Train the model
    model.fit(
        training,
        output,
        epochs=200,
        batch_size=16,
        validation_split=0.25,
        shuffle=True,
        verbose=1,
    )

    if save:
        model.save(r"model\potato.keras")

# train_ai(save=True)   Uncomment this if you want to train ai - set save to False if you dont wanna save the trained model!

def load_ai():
    """Load the model"""

    model = keras.models.load_model(r"model\potato.keras")
    return model

model = load_ai()

def _chatbot():
    """Chatbot"""

    while True:
        inp = input("User: ")
        inp = _clean_text(inp)  # clean input
        bag_of_words = _fuzzy_bag_of_words(inp, words)
        # Reshape the bag_of_words to match the model's input shape
        input_data = bag_of_words.reshape(1, -1)
        
        results = model.predict(input_data)  # predict the response
        results_index = argmax(results)
        if results_index < len(labels):
            tag = labels[results_index]

            if results[0][results_index] > 0.75:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                _typing_effect(f"Potato-GPT: {randomizer(responses)}")  # animation
                continue
        _typing_effect(randomizer(idk))  # animation
