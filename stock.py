import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import requests

"""
from tensorflow import keras
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense
from keras._tf_keras.keras.layers import LSTM
"""

# using practice data
df = pd.read_csv('data\Stock Market data\World-Stock-Prices-Dataset.csv', index_col='Date', parse_dates=True)



nvidiaData = df[df['Brand_Name'] == 'nvidia']
print(nvidiaData.head())

appleData = df[df['Brand_Name'] == 'apple']
print(appleData.head())

microsoftData = df[df['Brand_Name'] == 'microsoft']
print(microsoftData.head())

googleData = df[df['Brand_Name'] == 'google']
print(googleData.head())

print(len(df))
print((sum(df["High"] != df['Low'])))


""" daily updated stock market data
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=TO72VVPA7MUEIAZF'
r = requests.get(url)
data = r.json()

print(data)
"""
import kagglehub

# Download latest version
path = kagglehub.dataset_download("andrewmvd/sp-500-stocks")

print("Path to dataset files:", path)