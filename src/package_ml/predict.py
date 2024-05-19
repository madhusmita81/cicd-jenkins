import pandas as pd
import numpy as np
import joblib
from package_ml.config import config
from package_ml.processing.datahandling import load_data, load_pipeline

classification_pipeline= load_pipeline(config.MODEL_NAME)

def generate_predictions(data_input):
    data = pd.DataFrame(data_input)
    pred = classification_pipeline.predict(data[config.FEATURES])
    output = np.where(pred == 1, 'Y', 'N')
    result = {'prediction' : output}
    return result

def generate_test_predictions():
    data = pd.DataFrame(config.TEST_FILE)
    pred = classification_pipeline.predict(data[config.FEATURES])
    output = np.where(pred == 1, 'Y', 'N')
    result = {'prediction' : output}
    return result

# def generate_predictions():
#     data = pd.DataFrame(config.TEST_FILE)
#     pred = classification_pipeline.predict(data[config.FEATURES])
#     output = np.where(pred == 1, 'Y', 'N')
#     result = {'prediction' : output}
#     return result

if __name__ == '__main__':
    generate_predictions()