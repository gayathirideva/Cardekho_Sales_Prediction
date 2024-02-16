# -*- coding: utf-8 -*-
"""Cardekho_ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bQ4qPg_c_xK8_iKeAsNdS0FuISmJZAJC
"""

# Import Required libraries
import pandas as pd
import numpy as np
from scipy.stats import skew, randint
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error,  r2_score

import joblib
import pickle

df = pd.read_csv('/content/fi_df.csv') #/content/cardekho (1).csv
df

df.isnull().sum()

import pandas as pd
import re
import numpy as np

def alphanumeric_to_numeric(price_str):
    # Handling NaN values
    if pd.isna(price_str):
        return 0

    # Handle the case where the price is in the format "₹ 4 Lakh"
    match = re.match(r'^₹\s?([\d.]+)\s?Lakh$', price_str)

    if match:
        numeric_part = float(match.group(1))
        return int(numeric_part * 100000)  # Convert Lakh to numeric value
    else:
        # Use the general alphanumeric_to_numeric function
        return alphanumeric_to_numeric_general(price_str)

# Define a general function for alphanumeric to numeric conversion
def alphanumeric_to_numeric_general(price_str):
    multiplier_dict = {"thousand": 1000, "lakh": 100000, "million": 1000000}
    match = re.match(r'^([\d.]+)\s?(\w+)?$', price_str)

    if match:
        numeric_part = float(match.group(1))
        word_part = match.group(2)
        multiplier = multiplier_dict.get(word_part, 1)
        return int(numeric_part * multiplier)
    else:
        return None

# Example DataFrame with a 'Price' column containing values
#data = {'CarModel': ['Car1', 'Car2', 'Car3', 'Car4'],
       # 'Price': ['₹ 4 Lakh', '2.5 million', '4.8 thousand', np.nan]}

#df = pd.DataFrame(data)

# Apply the conversion function to the 'Price' column
df['price'] = df['price'].apply(alphanumeric_to_numeric)
df['priceActual'] = df['priceActual'].apply(alphanumeric_to_numeric)

# Display the original and numeric price columns
df

df.isnull().sum()

#df['priceActual'].fillna(df['priceActual'].median())

df['priceActual'].unique()

df['price'] = df['price'].fillna(df['price'].median())
#df['Seats'] = df['Seats'].fillna(df['Seats'].mean())

df['price'].unique()

#df['NumericPrice'].drop()
#df = df.drop(['NumericPrice', 'N_Price'], axis=1)

df['price'] = df['price'].fillna(df['price'].median())

#df['bt'].fillna('unknown', inplace=True)
#df['Insurance Validity'].fillna('unknown', inplace=True)
#df['RTO'].fillna('unknown',inplace=True)

#seats

df['Kms Driven'] = df['Kms Driven'].str.replace(' Kms', '').str.replace(',', '').astype(float)
df['Kms Driven'].fillna(df['Kms Driven'].mean(),inplace=True)

df['Engine Displacement'] = df['Engine Displacement'].str.replace(' cc', '').astype(float)
df['Engine Displacement'].fillna(df['Engine Displacement'].mean(),inplace = True)

df['Engine Displacement']

df

categorical_columns = df.select_dtypes(include=['object']).columns
categorical_columns

df.isnull().sum()

#df.isnull().sum() #bt , insurance validity, kms driven, RTO, Engine Displacement, seats

# Use pandas' get_dummies function for one-hot encoding
df_one_hot = pd.get_dummies(df, columns= categorical_columns, prefix=['bt_x', 'oem_x', 'model_x', 'variantName_x', 'Registration Year_x',
       'Insurance Validity_x', 'Fuel Type_x', 'RTO_x', 'Transmission_x', 'Safety_x',
       'Mileage_x', 'Max Power_x', 'Torque_x', 'Color_x', 'Engine Type_x', 'Max Torque_x',
       'Gear Box_x', 'Steering Type_x', 'Front Brake Type_x', 'Rear Brake Type_x',
       'Top Speed_x', 'Tyre Type_x'])

# Display the original and one-hot encoded columns
print(df_one_hot.head())

df_one_hot.describe().T

df_one_hot.skew()

#plt.figure(figsize=(16,8))
#sns.heatmap(df_one_hot.corr(), annot=True, cmap = 'coolwarm')
#plt.show()

df_one_hot.columns

df_one_hot.isnull().sum()

df_one_hot.to_csv('ml_file.csv', index=False)

dp_df = pd.read_csv('/content/ml_file.csv')
dp_df

dp_df.isnull().sum()
