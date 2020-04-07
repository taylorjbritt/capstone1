import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import os

def unpickle(filename):
    df = pd.read_pickle('../data/pickles/' + filename + '.pkl')
    return df

def moving_day_average(df, col_name, day_range = 9):
    col = np.arange(0,len(df)).reshape(-1,1)
    row = np.arange(0, day_range+1)
    mat = col + row
    windows = []
    for i in range(0, len(df) -10):
        index = range(mat[i][0], mat[i][day_range])
        windows.append(np.nanmean(df[col_name].iloc[index]))
    return windows

def q1_plotter(picklename, city_name, first_case_day = 0, shelter_day = 0, substance = 'no2', day_range = 9, firstyear = 2016):
    
    years = np.arange(firstyear, 2021, 1)
    #Turn the picklefile into a dataframe
    df =  unpickle(picklename)
    fig, ax = plt.subplots(figsize=(16,8))
    #plot the graph for each year
    for year in years:
        df_q1 = df[df['date'] > datetime.datetime(year-1, 12, 27)]
        df_q1 = df_q1[df_q1['date'] < datetime.datetime(year, 4, 6)]
        x = np.arange(0, len(df_q1)-10, 1)
        y = moving_day_average(df_q1, substance, day_range)
        if year == 2020:
            ax.plot(x, y, linewidth = 3, label = str(year))
        else:
            ax.plot(x, y, alpha = .5, label = str(year))
    title_ = f'{city_name} {substance} AQI Levels: {day_range} Day Averages for the first Quarters of {firstyear}-2020'
    ylabel_ = f'{substance} levels (AQI, {day_range} day moving averages)'
    save_name = '../images/' + picklename + substance + '.png'
    ax.set_title(title_)
    if first_case_day != 0:
        ax.axvline(x = first_case_day, ls='--', c='red', label = "First COVID Case in Region")
    if shelter_day != 0:
        ax.axvline(x = shelter_day, ls='--', label = "Shelter in Place Order")
    ax.set_xlabel('Days Into the Year')
    ax.set_ylabel(ylabel_)
    ax.legend(loc='best', ncol=3, fancybox=True, shadow=True)
    fig.savefig(save_name, dpi=125)

plot_dict = {
    'beijing': ['Beijing', 0, 0],
    'dallas': ['Dallas', 69, 82],
    'denver': ['Denver', 64, 83],
    'houston': ['Houston', 69, 84],
    'la': ['Los Angeles', 26, 83],
    'madrid' : ['Madrid', 31, 73],
    'nyc' : ['New York City', 61, 80],
    'oakland' : ['Oakland', 26, 76],
    'paris' : ['Paris', 24, 77],
    'santiago' : ['Santiago de Chile', 63, 86],
    'saopaulo' : ['São Paulo', 66, 81],
    'seattle' : ['Seattle', 21, 83],
    'wuhan' : ['Wuhan', 0, 0]
}
        
if __name__ == '__main__':
    for key in plot_dict.keys():
        name, first_case_day, shelter_day = plot_dict[key]
        q1_plotter(key, name, first_case_day, shelter_day)

    # q1_plotter('denver', 'Denver', 64, 83)
    # q1_plotter('wuhan', 'Wuhan', 0, 0)
    # q1_plotter('beijing', 'Beijing', 0, 0)
    # q1_plotter('beijing', 'Beijing', 0, 0)