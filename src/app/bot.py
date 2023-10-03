# Modules
from src.utils.training import _loader
from time import sleep
from random import choice as randomizer
from numpy import argmax, array
from fuzzywuzzy.fuzz import token_set_ratio
from keras.models import Sequential
from tensorflow import keras
from src.utils import preloader
from src.utils import useful
from colorama import Fore, Style
from src.utils import databasey
from src.utils.values import *


last_layer: int = len(databasey._tags_parser())

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
    s_doc = preloader.nlp(s)
    s_words = [token.lemma_ for token in s_doc if not token.is_punct]

    for se in s_words:
        for i, w in enumerate(words):
            if token_set_ratio(w, se) >= 70:
                bag[i] = 1

    return array(bag)


def _typing_effect(text):
    """ CLI bot typing effects"""

    for char in text:
        print((Fore.CYAN + char + Style.RESET_ALL), end="", flush=True)
        sleep(0.05)
    print("\n")



model = Sequential() # Defining model


def train_ai(save: bool=False):
    """Train the model"""

    useful._info_text("Starting the training of Potato-GPT model...")
    # Input Layer
    model.add(keras.layers.InputLayer(input_shape=(None, len(training[0]))))

    # First Layer
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
        units=64,
        activation='relu',
        use_bias=True
    ))

    model.add(keras.layers.Dense(
        units=last_layer,
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
        epochs=150,
        batch_size=12,
        validation_split=0.15,
        shuffle=True,
        verbose=1,
    )

    
    model.summary()

    if save:
        useful._info_text("Saving Potato-GPT model...")
        model.save(model_path)

train_ai(save=True) # - Uncomment to train ai

def load_ai():
    """Load the model"""
    try:
        useful._info_text("Loading Potato-GPT model...")
        model = keras.models.load_model(model_path)
        model.summary()
        useful._info_text("Done Loading Potato-GPT model...")
        return model
    
    except:
        train_ai(True)

        

#model = load_ai() # Load ai if there ai

def _chatbot():
    """Chatbot"""

    useful._info_text("Potato-GPT connected...")

    while True:
        inp = useful._input_text(f"{user_username}: ")
        #inp = preloader._text_cleaner_v2(inp)  # clean input
        print(inp)
        bag_of_words = _fuzzy_bag_of_words(inp, words)
        # Reshape the bag_of_words to match the model's input shape
        input_data = bag_of_words.reshape(1, -1)
        
        results = model.predict(input_data)  # predict the response
        results_index = argmax(results)

        if results_index < len(labels):
            tag = labels[results_index]

            if results[0][results_index] > 0.40: # Increase value to increase accuracy - Can also make bot limited
                responses = databasey._responses_parser(tag) 

                _typing_effect(f"{bot_username}: {randomizer(responses)}")  # animation
                continue

        _typing_effect(f"{bot_username}: {randomizer(idk)}")  # animation
