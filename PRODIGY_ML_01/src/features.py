import pandas as pd

def prepare_features(df):
    df["TotalBath"] = df["FullBath"] + 0.5 * df["HalfBath"]
    features = ["GrLivArea", "BedroomAbvGr", "TotalBath"]
    X = df[features]
    y = df["SalePrice"]
    return X, y
