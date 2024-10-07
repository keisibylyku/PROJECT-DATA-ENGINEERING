import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from collections import Counter

# Ignore warnings
warnings.filterwarnings('ignore')

# Set Seaborn style
sns.set(style='whitegrid')

# Title for the Streamlit app
st.title("GOLD LAYER REPORTS FOR MOVIES")
