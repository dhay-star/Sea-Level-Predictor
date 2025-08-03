import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # 3. First line of best fit (1880–2050)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = res1.slope * x1 + res1.intercept
    plt.plot(x1, y1, 'r', label='Best Fit Line: 1880–2050')

    # 4. Second line of best fit (2000–2050)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = res2.slope * x2 + res2.intercept
    plt.plot(x2, y2, 'g', label='Best Fit Line: 2000–2050')

    # 5. Customize plot
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # 6. Save and return plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
