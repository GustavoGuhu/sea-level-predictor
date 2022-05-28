from re import X
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Create scatter plot

    plt.scatter(x, y)

    # Create first line of best fit
    xl = np.arange(df["Year"].min(),2051,1)
    res = linregress(x, y)
    yl = res.intercept + res.slope*xl
    plt.plot(xl, yl, label='fitted line 1', color ='red')

    # Create second line of best fit
    df = df.loc[df['Year'] >= 2000]
    xl2 = np.arange(df["Year"].min(),2051,1)
    res2 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    yl2 = res2.intercept + res2.slope*xl2
    plt.plot(xl2, yl2, label='fitted line 2')
    
    # Add labels and title
    plt.xlim(1850,2075)
    plt.legend()
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png', dpi = 800)
    return plt.gca()