# Imports & Setup

import warnings

import pandas as pd
import numpy as np
import seaborn as sns
import joblib
import sweetviz as sv

from matplotlib import pyplot as plt
from src.utils import *
from src.globals import *

import difflib

plt.rcParams["figure.figsize"] = (8,4)

warnings.filterwarnings('ignore')