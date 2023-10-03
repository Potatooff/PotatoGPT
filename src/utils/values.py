import configparser
from src.utils.paths import *

config = configparser.ConfigParser()
config.read(plastic_ini) # Read the setting file

# * Get the values from the setting file

general: str = "user_info"
server: str = "server_info"


# * General settings
bot_username: str = config.get(general, "bot_name")
user_username: str = config.get(general, "username")

# * Server settings

nltk_install_check: str = config.get(server, "nltk_installation")
model_path: str = rf'{config.get(server, "model_path")}'
trained_data_path: str = rf'{config.get(server, "trained_data_path")}'
raw_data_path: str = rf'{config.get(server, "raw_data_path")}'
raw_database_path: str = rf'{config.get(server, "raw_database_path")}'
initialization: str = config.get(server, "initialization")


def _rewrite_plastic_values(tag: str, variable: str, value: str) -> None:
    """Change the values of the setting file!\n
    args:
        tag: str - The tag of the variable to change
        variable: str - The variable value name\n
        value: str - The new value\n
    returns: None
    """

    config.set(tag, variable, value)
    with open(plastic_ini, 'w') as configfile:
        config.write(configfile)
        configfile.close()