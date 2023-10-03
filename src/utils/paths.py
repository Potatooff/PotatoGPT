from os import getcwd, path


main_path: str = getcwd() # main project path

data_folder: str = path.join(main_path, 'data')
# * Subfolders of data folder
data_db: str = path.join(data_folder, 'data.db')
data_json: str = path.join(data_folder, 'intents.json')
trained_data: str = path.join(data_folder, 'trained_data.pickle')


model_folder: str = path.join(main_path, 'model')
# * Subfolders of model folder
model_keras: str = path.join(model_folder, 'potato.keras')


settings_folder: str = path.join(main_path, 'settings')
# * Subfolders of settings folder
plastic_ini: str = path.join(settings_folder, 'plastic.ini')


