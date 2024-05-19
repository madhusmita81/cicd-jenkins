## we can cross validate as when required, validate together by setting up the parameters as well , so we have to create the pipeline

from sklearn.pipeline import Pipeline
from package_ml.config import config
from package_ml.processing import preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

classification_pipeline= Pipeline(
    [
        ('MeanImputation', pp.MeanImputer(variables= config.NUM_FEATURES)),
        ('ModeImputation', pp.ModeImputer(variables= config.CAT_FEATURES)),
        ('DomainPreprocessing', pp.DomainProcessing(
            variable_to_add= config.FEATURES_TO_ADD,
            variable_to_modify= config.FEATURES_TO_MODIFY)),
        ('DropFeatures', pp.DropColumns(variables= config.DROP_FEATURES)),
        ('LabelEncoder', pp.CustomLabelEncoder(variables= config.FEATURES_TO_ENCODE)),
        ('LogTrans', pp.LogTransform(variables= config.LOG_FEATURES)),
        ('Scaler', MinMaxScaler()),
        ('Model', LogisticRegression(random_state= 42))

    ]
)