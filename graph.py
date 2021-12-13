import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# create a results directory if it does not exist
os.makedirs(os.path.dirname('./Results/'), exist_ok=True)

# Read the csv
def read_csv(file):
    file = pd.read_csv(file, skiprows=8, usecols= list(range(6,29)))
    file = file[~file.isin([np.nan, np.inf, -np.inf]).any(1)]
    return file

# graphs unemployment rate
def get_rates(file):
    return np.array(file)[6].astype('float64'), np.array(file)[7].astype('float64')

# plots
def plot_files(x,files,index):
    for files in files:
         plt.plot(x,files[index])

# .csvs are in this location
f1 = './Data/Entire_Labor_Force.csv'
f2 = './Data/15-19.csv'
f3 = './Data/20-24.csv'
f4 = './Data/25-54.csv'
f5 = './Data/55-64.csv'
ageGroup = ['Entire Labor Force', '15-19', '20-24', '25-54', '55-64']

# read each file
f1 = read_csv(f1)
f2 = read_csv(f2)
f3 = read_csv(f3)
f4 = read_csv(f4)
f5 = read_csv(f5)

# load our x values (which are dates)
x =list(f1.columns)
x = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in x]


files= []  
# add tuples to list
for file in [f1,f2,f3,f4,f5]:
    files.append(get_rates(file))

# get tuples seperately
f1, f12 = get_rates(f1)
f2, f22 = get_rates(f2)
f3, f32 = get_rates(f3)
f4, f42 = get_rates(f4)
f5, f52 = get_rates(f5)

# graph set up
plt.figure(1)
plt.title("Unemployment Rate by Age Groups in Canada")    
plt.xlabel("Dates")
plt.ylabel("Unemployment Rate")
plt.legend(['Entire Labor Force', 'Ages 15-19','Ages 20-24','Ages 25-54','Ages 55-64'], loc = "upper right",bbox_to_anchor=(.4,-.2))
plt.gcf().autofmt_xdate()
plt.tight_layout()

# plot and save
plot_files(x,files, 0)
plt.savefig('./Results/Unemployment Rate Graph.jpg')

# graph2 set up
plt.figure(2)
plt.title("Employment Rate by Age Groups in Canada")    
plt.xlabel("Dates")
plt.ylabel("Employment Rate")
plt.legend(['Entire Labor Force', 'Ages 15-19','Ages 20-24','Ages 25-54','Ages 55-64'], loc = "upper right",bbox_to_anchor=(.4,-.2))
plt.gcf().autofmt_xdate()
plt.tight_layout()

# plot and save
plot_files(x,files, 1)
plt.savefig('./Results/Employment Rate Graph.jpg')
#plt.show()


# Collect Covid Cases
my_filtered_csv = pd.read_csv('./Data/cases_timeseries_canada.csv', usecols=['date_report','Monthly cases'])
columns = (my_filtered_csv[~my_filtered_csv['date_report'].isna()])

# store covid cases in y (unrelated dataset)
y = [] 
columns = list(zip(columns['date_report'], columns['Monthly cases']))
for i in columns:
    y.append(i[1])

plt.figure(0)
plt.title("Number of Canada Covid-19 Cases by Month")    
plt.xlabel("Dates")
plt.ylabel("Number of Cases")

plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.savefig('./Results/Covid Cases Graph.jpg')
#plt.show()

# split the arrays after october (f1 = file 1; f12= file 1 part 2)
y,y1 = y[0:10], y[10:]
x,x1 = x[0:10], x[10:]
f1,f12 = f1[0:10], f1[10:]
f2,f22 = f2[0:10], f2[10:] 
f3,f32 = f3[0:10], f3[10:]
f4,f42 = f4[0:10],f4[10:]
f5,f52 = f5[0:10],f5[10:]

# prep for output files
arr1 = []
arr2 = []
arr1 = np.append(arr1, [np.corrcoef(f1,y)[0][1],np.corrcoef(f2,y)[0][1],np.corrcoef(f3,y)[0][1],np.corrcoef(f4,y)[0][1],np.corrcoef(f5,y)[0][1]])
arr2 = np.append(arr2, [np.corrcoef(f12,y1)[0][1],np.corrcoef(f22,y1)[0][1],np.corrcoef(f32,y1)[0][1],np.corrcoef(f42,y1)[0][1],np.corrcoef(f52,y1)[0][1]])

# extend length to match Time Series 1
while(len(y) != len(arr1)):
    arr1 = np.append(arr1, '')
    ageGroup = np.append(ageGroup, '')


# create output file
df = pd.DataFrame({"TimeSeries 1" : x, "# of Covid Cases" : y, "15 and Over": f1,"15-19": f2,"20-24": f3,"25-54": f4,"55-64": f5, "Age Groups": ageGroup, "Correlation": arr1})
df.to_csv("./Results/Timeseries 1 Unemployment Eval.csv", index=False, mode='w')

# extend length to math Time Series 2
while(len(y1) != len(arr2)):
    arr2 = np.append(arr2, '')
while(len(arr2) != len(ageGroup)):
    ageGroup = np.append(ageGroup, '')

df =  pd.DataFrame({"TimeSeries 2" : x1, "# of Covid Cases" : y1, "15 and Over": f12,"15-19": f22,"20-24": f32,"25-54": f42,"55-64": f52, "Age Groups": ageGroup, "Correlation": arr2})
df.to_csv("./Results/Timeseries 2 Unemployment Eval.csv", index=False, mode='w')