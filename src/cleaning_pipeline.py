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
    #df['pm10'] = pd.to_numeric(df[' pm10'])
   #df['o3'] = pd.to_numeric(df[' o3'])
    df['no2'] = pd.to_numeric(df[' no2'])
    #df['co'] = pd.to_numeric(df[' co'])
    # df_clean = df.drop(' pm25', axis = 1).drop(' pm10', axis = 1).drop(' o3', axis = 1).drop(' no2', axis = 1).drop(' so2', axis = 1).drop(' co', axis = 1)
    df_clean = df.drop(' pm25', axis = 1).drop(' no2', axis = 1)
    return df_clean

def pickler(df, new_filename):
    filepath = "../data/pickles/" + str(new_filename) + ".pkl"
    df.to_pickle(filepath)

def clean_pipeline(filename, new_filename):
    raw_df = import_csv(filename)
    dated_df = datetime_df(raw_df)
    nan_df = nan(dated_df)
    clean_df = numvals(nan_df)
    pickler(clean_df, new_filename)
    print(f'The {new_filename} pickles are in the fridge!')

# 'aurora-hills visitor center, northern virginia, usa-air-quality.csv' : 'dc',

file_picklename_dict = {

'beacon-hill, seattle, washington, usa-air-quality.csv' : 'seattle',
'beijing-air-quality.csv' : 'beijing',
'clinton,-houston, texas-air-quality.csv' : 'houston',
'dallas-hinton, fort worth, dallas, texas-air-quality.csv' : 'dallas',
'gary-iitri,-indiana, usa-air-quality.csv' : 'gary',
'i-25-denver, colorado, usa-air-quality.csv' : 'denver',
'los-angeles-north main street-air-quality.csv' : 'la',
'madrid-air-quality.csv' : 'madrid',
'milano-pascal città studi, lombardia, italy-air-quality.csv' : 'milan',
'oakland-- west, alameda, california-air-quality.csv' : 'oakland',
'paris-air-quality.csv' : 'paris',
'parque-d.pedro ii, são paulo, brazil-air-quality.csv' : 'saopaulo',
'parque-o\'higgins, chile-air-quality.csv' : 'santiago',
'chullora-sydney east, australia-air-quality.csv' : 'sydney',
'queens-college, new york, usa-air-quality.csv' : 'nyc',
'wuhan-air-quality (1).csv' : 'wuhan'}
   


if __name__ == '__main__':
    #clean_pipeline('i-25-denver, colorado, usa-air-quality.csv', 'denver')

    # for filename in file_picklename_dict.keys():
    #     clean_pipeline(filename, file_picklename_dict[filename])


    clean_pipeline('major-dhyan chand national stadium, delhi, delhi, india-air-quality.csv', 'newdehli')
    
