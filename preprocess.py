import pandas as pd

def preprocess_data(df):

    df=df.dropna()
    x=df.drop("Price",axis=1)
    y=df["Price"]

    return x,y


