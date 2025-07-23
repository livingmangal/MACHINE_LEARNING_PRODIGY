import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    return pd.read_csv(path)

def select_data(data):
    return data[['Spending Score (1-100)']]

def scale_data(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)
