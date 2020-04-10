#I ended up not using this function, but the idea was to test the two different null hypotheses:
#that the values for 2020 and previous years from BEFORE the quarantine date were the same, and 
# that the values AFTER that same date were the same. However, I have doubts about the statistical 
#soundness of the test, and it basically always returned a p-value below .05, so I didn't include 
#it in the markdown.

import scipy.stats as stats
import pandas as pd
import numpy as np

plot_dict = {
    'beijing': ['Beijing', 0, 0],
    'denver': ['Denver', 63, 82],
    'la': ['Los Angeles', 25, 82],
    'madrid' : ['Madrid', 30, 72],
    'milan' : ['Milan', 31, 68],
    'nyc' : ['New York City', 60, 79],
    'oakland' : ['Oakland', 25, 75],
    'paris' : ['Paris', 23, 78],
    'santiago' : ['Santiago de Chile', 62, 85],
    'saopaulo' : ['São Paulo', 65, 80],
    'seattle' : ['Seattle', 20, 82],
    'sydney' : ['Sydney', 31, 88],
    'wuhan' : ['Wuhan', 0, 22]
    }



def t_tester(picklename, sep_date, part = 'no2'):
    df = unpickle(picklename)
    df['year'] = df['date'].dt.year
    df['day_of_year'] = df['date'].dt.dayofyear
    a = df[df['year'] < 2020]
    a = a[a['day_of_year'] < quardate]
    b = df[df['year'] == 2020]
    b = b[b['day_of_year'] < quardate]
    c = df[df['year'] >= 2020]
    c = c[c['day_of_year'] < quardate]
    d = df[df['year'] == 2020]
    d = d[d['day_of_year'] >= quardate]
    a_np = a[part].dropna().to_numpy()
    b_np = b[part].dropna().to_numpy()
    c_np = c[part].dropna().to_numpy()
    d_np = d[part].dropna().to_numpy()
    before_t_stat, before_p_val = stats.ttest_ind(a_np, b_np, axis=0, equal_var=False)
    after_t_stat, after_p_val = stats.ttest_ind(c_np, d_np, axis=0, equal_var=False)
    print(f' The following results are for: {picklename}')
    print(f'Prior to the date, the t-statistic was {before_t_stat:.4f} and the p-value was {before_p_val:.4f}.')
    print(f'After to the date, the t-statistic was {after_t_stat:.4f} and the p-value was {after_p_val:.4f}.')
    print(' ')

if __name__ == '__main__':

    for key in plot_dict.keys():
        t_tester(key, plot_dict[key][2])
    