from src.app.bot import _chatbot
#from src.ai.main import main_page
from os import environ
#from src.utils.values import bot_username
from src.utils.first_run import _initialize



if __name__ == "__main__":
    environ["OMP_NUM_THREADS"] = "3"
    #_initialize()
    _chatbot()
    #main_page().mainloop()
    