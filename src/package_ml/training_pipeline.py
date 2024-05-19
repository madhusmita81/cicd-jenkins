import pandas as pd
import numpy as np

from pathlib import Path
import os
import sys

# # Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from package_ml.config import config
from package_ml.processing.datahandling import load_data, save_pipeline
from package_ml.processing import preprocessing as pp
from package_ml import pipeline as pipe
import sys

def model_training():
    dTrain= load_data(config.TRAIN_FILE)
    yTrain= dTrain[config.TARGET].map({'N' : 0, 'Y' : 1})
    pipe.classification_pipeline.fit(dTrain[config.FEATURES], yTrain)
    save_pipeline(pipe.classification_pipeline)

if __name__ == '__main__':
    model_training()

