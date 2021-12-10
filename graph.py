import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

my_filtered_csv = pd.read_csv('./Data/cases_timeseries_canada.csv', usecols=['date_report','Monthly cases'])
#df = pd.read_csv(csv_file)
#saved_column = df['date_report'] #you can also use df['column_name']

columns = (my_filtered_csv[~my_filtered_csv['date_report'].isna()])#,(my_filtered_csv[~my_filtered_csv['Monthly cases']. isna()])
#names = df.Names
x = []
y = [] 
z= []
columns = list(zip(columns['date_report'], columns['Monthly cases']))
for i in columns:
    x.append(datetime.datetime.strptime(i[0], '%Y-%m-%d').date())
    y.append(i[1])
    
plt.title("Number of Canada Covid-19 Cases by Month")    
plt.xlabel("Dates")
plt.ylabel("Number of Cases")
ypoints = y
xpoints = x
print(columns)
print(x)
plt.plot(x,y)

plt.gcf().autofmt_xdate()

plt.show()
'''with open('./Data/cases_timeseries_canada.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

    print(rows[7])
    print(rows[8])'''

