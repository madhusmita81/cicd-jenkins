import pathlib
import os
import package_ml

#fetching package path when called
# PACKAGE_ROOT= pathlib.Path(package_ml.__file__).resolve().parent
# PACKAGE_ROOT= os.getcwd()

PACKAGE_ROOT = pathlib.Path(os.path.abspath(os.path.dirname(__file__))).parent

DATA_PATH= os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_models')

TARGET = 'Loan_Status'

#Final features used in the model
FEATURES= ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender',  'Married',  'Dependents',  'Education',  'Self_Employed',  'Credit_History', 
                 'Property_Area']

FEATURES_TO_ENCODE= ['Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'Credit_History',
 'Property_Area']

FEATURES_TO_MODIFY = ['ApplicantIncome']

FEATURES_TO_ADD= 'CoapplicantIncome'

DROP_FEATURES= ['CoapplicantIncome']

LOG_FEATURES = ['ApplicantIncome', 'LoanAmount'] # taking log of numerical columns