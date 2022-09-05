# Imports & Setup

import sys
import warnings

import pandas as pd
import numpy as np
import seaborn as sns
import joblib

from matplotlib import pyplot as plt
from utils import POSITION_MAPPING, FOOTEDNESS_MAPPING, name_to_id, name_char_replacer, approximate_age_2020
import difflib

PROJECT_FOLDER = '/home/ricardo/coding/data-science/projects/predict_value_change_from_fm_data/'

sys.path.insert(0, PROJECT_FOLDER)

plt.rcParams["figure.figsize"] = (15,8)

warnings.filterwarnings('ignore')