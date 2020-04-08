import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import os

plt.style.use('ggplot')

#dictionary where the keys are the name of the picklefile,
# and the values are a list of 
# 1) how the city name should appear on the graph
# 2) the number of days into the year that the state (or country if outside the US)
# had its first case of covid (0 = the value won't display)
# 3) the number of days into the year that the city implemented 
# a quarantine or shelter in place (0 = the value won't display)
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
    'sydney' : ['Sydney', 32, 89],
    'wuhan' : ['Wuhan', 0, 23]
    }

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

# this will return scatterplots for pm2.5 and n02 concentrations for the picklefile passed in
def scatter_concentrations(picklename, city_name):
    df = unpickle(picklename)
    save_name = '../images/scatterplots/scatter' + picklename + '.png'
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(2,1,1)
    ax.scatter(df['date'], df['pm25'], label = "PM2.5" )
    ax.set_title(city_name +" "+ 'Air Quality Index - PM2.5')
    ax.set_ylim(0, (df['pm25'].max()*1.1))
    ax.legend(loc='best')
    fig.tight_layout(pad=1)
    ax = fig.add_subplot(2,1,2)
    ax.scatter(df['date'], df['no2'], label = "NO2" )
    ax.set_title(city_name +" "+ 'Air Quality Index - NO2')
    ax.set_ylim(0, (df['no2'].max()*1.1))
    ax.legend(loc='best')
    fig.tight_layout(pad=1)
    fig.savefig(save_name, dpi=125)


#this function will plot moving day average  values for NO2 (default) or PM25 for the first 3 months of each year
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
    save_name = '../images/quarterly_plots/q1' + picklename + substance + '.png'
    ax.set_title(title_)
    if first_case_day != 0:
        ax.axvline(x = first_case_day, ls='--', c='red', label = "First COVID Case in Region")
    if shelter_day != 0:
        ax.axvline(x = shelter_day, ls='--', label = "Shelter in Place Order")
    ax.set_xlabel('Days Into the Year')
    ax.set_ylabel(ylabel_)
    ax.legend(loc='best', ncol=3, fancybox=True, shadow=True)
    fig.savefig(save_name, dpi=125)


if __name__ == '__main__':
    for key in plot_dict.keys():
        name, first_case_day, shelter_day = plot_dict[key]
        q1_plotter(key, name, first_case_day, shelter_day)
    
    for key in plot_dict.keys():
        name, first_case_day, shelter_day = plot_dict[key]
        scatter_concentrations(key, name)

    
    
    # for key in plot_dict.keys():
    #     name, first_case_day, shelter_day = plot_dict[key]
    #     q1_plotter(key, name, first_case_day, shelter_day, 'pm25')

    # q1_plotter('denver', 'Denver', 64, 83)
    # q1_plotter('wuhan', 'Wuhan', 0, 0)
    # q1_plotter('beijing', 'Beijing', 0, 0)
    # q1_plotter('beijing', 'Beijing', 0, 0)