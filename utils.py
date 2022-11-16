import pandas as pd
import numpy as np

def process_future_data(path):
    df = pd.read_csv(path).dropna()

    df = df[::-1]
    df.columns = ['tic', 'date', 'open', 'high', 'low', 'close', 'Change', '%Chg','volume', 'Open Int']
    df['date'] = pd.to_datetime(df['date'])
    df['day']  = df['date'].dt.dayofweek
    df['tic']  = df['tic'].loc[0][:2]
    df = df.drop(['Change','%Chg','Open Int'],axis=1)
    df['adjcp'] = df['close']
    df = df[['date', 'open', 'high', 'low', 'close', 'adjcp', 'volume', 'tic','day']]
    df.reset_index(inplace=True,drop= True)
    
    return df
