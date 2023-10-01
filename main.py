from src.app.bot import _chatbot
#from src.ai.main import main_page
from os import environ

if __name__ == "__main__":
    environ["OMP_NUM_THREADS"] = "3"
    _chatbot()
    #main_page().mainloop()
