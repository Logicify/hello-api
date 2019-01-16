"""
CI Environment Settings
"""
from .settings_prod import *


DEBUG = (os.environ.get('DEBUG', 'False') in ['True', 'true', 'Yes', 'yes', '1'])


EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX', 'Logicify Microservice CI: ')
