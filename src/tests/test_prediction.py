import pytest
from package_ml.config import config
from package_ml.processing.datahandling import load_data
from package_ml.predict import generate_predictions

# output is not null
# output is str data type
# output is Y for an example data

@pytest.fixture
def single_prediction():
    test_data= load_data(config.TEST_FILE)
    single_row = test_data[ : 1]
    result = generate_predictions(single_row)
    return result

def test_notnull(single_prediction):
    assert single_prediction is not None

def test_strtype(single_prediction):
    assert isinstance(single_prediction.get('prediction')[0] , str)

def test_validate(single_prediction):
    assert single_prediction.get('prediction')[0] == 'Y'



