import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_csv(file):
    file = pd.read_csv(file, skiprows=8, usecols= list(range(6,29)))
    file = file[~file.isin([np.nan, np.inf, -np.inf]).any(1)]
    return file

def graph_employment_rate(file):
    return np.array(file)[6].astype('float64')

def plot_graph(x,y):
    plt.plot(x,y)

global f1 # every DS
global f2 # 15-19 DS
global f3 # 20-24 DS
global f4 # 25-54 DS
global f5 # 55-65 DS


f1 = './Data/Entire_Labor_Force.csv'
f2 = './Data/15-19.csv'
f3 = './Data/20-24.csv'
f4 = './Data/25-54.csv'
f5 = './Data/55-64.csv'
f1 = read_csv(f1)
f2 = read_csv(f2)
f3 = read_csv(f3)
f4 = read_csv(f4)
f5 = read_csv(f5)
#my_filtered_csv = pd.read_csv('./Data/15-19.csv', skiprows=8, usecols= list(range(6,28)))

pd.set_option("display.max_rows", 0, "display.max_columns", 0)
#my_filtered_csv = my_filtered_csv[~my_filtered_csv.isin([np.nan, np.inf, -np.inf]).any(1)]
x=list(f1.columns)
x= [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in x]
f1 = graph_employment_rate(f1)
f2 = graph_employment_rate(f2)
f3 = graph_employment_rate(f3)
f4 = graph_employment_rate(f4)
f5 = graph_employment_rate(f5)
'''print(f1)
print(f2)
print(f3)
print(f4)
print(f5)'''



plot_graph(x,f1)
plot_graph(x,f2)
plot_graph(x,f3)
plot_graph(x,f4)
plot_graph(x,f5)


plt.show()