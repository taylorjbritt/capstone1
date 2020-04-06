import pandas as pd
import numpy as np
import datetime
import os


#import the csv file as a dataframe
def import_csv(filename):
    df_raw = pd.read_csv('../data/' + filename)
    return df_raw


#change the date values to datetime
def datetime_df(df):
    df['date']= pd.to_datetime(df['date'])
    df_time = df.sort_values('date')
    return df_time

#replace columns with empty spaces with NaN values
def nan(df):
    df_nan = df.replace(" ", np.NaN)
    return df_nan

#convert the string values in each column to numeric values,
#remove the spaces at the beginning of the column names
#and drop the old columns
def numvals(df):
    df['pm25'] = pd.to_numeric(df[' pm25'])
    df['pm10'] = pd.to_numeric(df[' pm10'])
    df['o3'] = pd.to_numeric(df[' o3'])
    df['no2'] = pd.to_numeric(df[' no2'])
    df['co'] = pd.to_numeric(df[' co'])
    df_clean = df.drop(' pm25', axis = 1).drop(' pm10', axis = 1).drop(' o3', axis = 1).drop(' no2', axis = 1).drop(' so2', axis = 1).drop(' co', axis = 1)
    return df_clean

def pipeline(filename):
    raw_df = import_csv(filename)
    dated_df = datetime_df(raw_df)
    nan_df = nan(dated_df)
    clean_df = numvals(nan_df)
    return clean_df

if __name__ == __main__: