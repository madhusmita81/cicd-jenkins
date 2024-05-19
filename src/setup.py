from setuptools import setup, find_packages
import os 
import io 
from pathlib import Path

#Metadata of package
NAME = "package_ml"
DESCRIPTION = "Loan Prediction Model"
URL = "https://github.com/madhusmita81"
EMAIL = "madhu8000000@gmail.com"
AUTHOR= 'Madhu'
REQUIRES_PYTHON = '>=3.10.14'

# pwd = os.path.abspath(os.path.dirname(__file__))
# pwd= os.getcwd()

# pwd= os.path.dirname(os.path.realpath('__file__'))
pwd = os.path.abspath(os.path.dirname(__file__))

def list_reqs(fname= 'requirements.txt'):
    with io.open(os.path.join(pwd, fname), encoding='utf-8') as f:
        return f.read().splitlines()

try:
    with io.open(os.path.join(pwd, 'README.md'), encoding= 'utf-8') as f:
        long_desc= '\n' + f.read()

except FileNotFoundError:
    long_desc = DESCRIPTION

#load version.py module as a dict
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about= {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name= NAME,
    _version = about['__version__'],
    description= DESCRIPTION,
    long_description= long_desc,
    long_description_content_type = 'text/markdown',
    author= AUTHOR,
    author_email= EMAIL,
    python_requires= REQUIRES_PYTHON,
    url= URL,
    packages= find_packages(exclude= ('tests', )),
    package_data= {'prediction_model': ['VERSION']},
    install_requires= list_reqs(),
    extras_require= {},
    include_package_data= True,
    license= 'MIT',
    classifiers= [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10.14',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'

    ]
)
