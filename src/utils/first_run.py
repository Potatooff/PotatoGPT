from src.utils.values import _rewrite_plastic_values, initialization, server
from src.utils.preloader import _download_nltk_stopwords
from src.utils.paths import *


def paths_setup():
    try:
        _rewrite_plastic_values(server, "model_path", model_keras)
        _rewrite_plastic_values(server, "raw_database_path", data_db)
        _rewrite_plastic_values(server, "raw_data_path", data_json)
        _rewrite_plastic_values(server, "trained_data_path", trained_data)
        return True
    except:
        return "An error occured with the initialization setup!"

def _initialize() -> None:

    if initialization == "True":
        print("PROGRAM SETTING UP...")
        try: 
            bar: bool = _download_nltk_stopwords

            if bar:
                _rewrite_plastic_values(server, "nltk_installation", "True")
            else:
                print("An error occured while installing nltk")

            foo: bool = paths_setup()

            if foo:
                print("Successfully setup paths!")
            else:
                print("An error occured while setting up paths")

            if foo and bar:
                _rewrite_plastic_values(server, "initialization", "False")
            else:
                _rewrite_plastic_values(server, "initialization", "True")

        except Exception as e:
            print("AN ERROR OCCURED!")

    else:
        print("NO SETUP REQUIRED!")
        pass