import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
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
global f5 # 55-64 DS


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


plt.title("Employment Rate by Age Groups in Canada")    
plt.xlabel("Dates")
plt.ylabel("Employment Rate")

plot_graph(x,f1)
plot_graph(x,f2)
plot_graph(x,f3)
plot_graph(x,f4)
plot_graph(x,f5)

plt.legend(['Entire Labor Force', 'Ages 15-19','Ages 20-24','Ages 25-54','Ages 55-64'], loc = "upper right")
plt.gcf().autofmt_xdate()
plt.show()'''


#now that we have displayed everything lets find a systematic way
my_filtered_csv = pd.read_csv('./Data/cases_timeseries_canada.csv', usecols=['date_report','Monthly cases'])
columns = (my_filtered_csv[~my_filtered_csv['date_report'].isna()])#,(my_filtered_csv[~my_filtered_csv['Monthly cases']. isna()])
#names = df.Names
x = []
y = [] 
z= []
columns = list(zip(columns['date_report'], columns['Monthly cases']))
for i in columns:
    x.append(datetime.datetime.strptime(i[0], '%Y-%m-%d').date())
    y.append(i[1])

prev = 0
index = 0
count = 0
for i in y:
    if(prev >0 and i > prev):
        #call some function
        print(index, prev, i)
        count +=1

    prev = i
    index+=1
print('Covid increased cases increased ' +str(count) +' times')

count2 = 0
index = 0
for i in y:
    if(prev >0 and i < prev):
        #call some function
        print(index, prev, i)
        count2 +=1

    prev = i
    index+=1
print('Covid increased cases decreased ' +str(count2) +' times')