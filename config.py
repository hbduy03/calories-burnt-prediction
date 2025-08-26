import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR,'calories','model', 'calo_model.pkl')
DATA1_PATH = os.path.join(BASE_DIR,'calories','data','calories.csv')
DATA2_PATH = os.path.join(BASE_DIR,'calories','data','exercise.csv')
RECORD_PATH = os.path.join(BASE_DIR,'calories','data','user.csv')
