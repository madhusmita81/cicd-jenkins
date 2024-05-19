import os
import pandas as pd
import joblib
from package_ml.config import config

#load data
def load_data(file_name):
    file_path= os.path.join(config.DATA_PATH, file_name)
    _data= pd.read_csv(file_path)
    return _data

#Serialization
def save_pipeline(pipeline_to_save):
    save_path= os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print(f"Model has been saved under the name {config.MODEL_NAME}")

#deserialization
def load_pipeline(pipeline_to_load):
    save_path= os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    model= joblib.load(save_path)
    print(f"Model {config.MODEL_NAME} has been loaded")
    return model

