import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the csv
def read_csv(file):
    file = pd.read_csv(file, skiprows=8, usecols= list(range(6,29)))
    file = file[~file.isin([np.nan, np.inf, -np.inf]).any(1)]
    return file

# graphs unemployment rate
def graph_unemployment_rate(file):
    return np.array(file)[6].astype('float64')

# plots
def plot_graph(x,y):
    plt.plot(x,y)


# .csvs are in this location
f1 = './Data/Entire_Labor_Force.csv'
f2 = './Data/15-19.csv'
f3 = './Data/20-24.csv'
f4 = './Data/25-54.csv'
f5 = './Data/55-64.csv'

# read each file
f1 = read_csv(f1)
f2 = read_csv(f2)
f3 = read_csv(f3)
f4 = read_csv(f4)
f5 = read_csv(f5)

 #for debugging
#pd.set_option("display.max_rows", 0, "display.max_columns", 0)

# load our x values (which are dates)
x =list(f1.columns)
x = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in x]

# graph each point
f1 = graph_unemployment_rate(f1)
f2 = graph_unemployment_rate(f2)
f3 = graph_unemployment_rate(f3)
f4 = graph_unemployment_rate(f4)
f5 = graph_unemployment_rate(f5)

# graph set up
plt.title("Unemployment Rate by Age Groups in Canada")    
plt.xlabel("Dates")
plt.ylabel("Unemployment Rate")

plot_graph(x,f1)
plot_graph(x,f2)
plot_graph(x,f3)
plot_graph(x,f4)
plot_graph(x,f5)


plt.legend(['Entire Labor Force', 'Ages 15-19','Ages 20-24','Ages 25-54','Ages 55-64'], loc = "upper right",bbox_to_anchor=(.4,-.2))
plt.gcf().autofmt_xdate()
plt.tight_layout()
#plt.show()


# Collect Covid Cases
my_filtered_csv = pd.read_csv('./Data/cases_timeseries_canada.csv', usecols=['date_report','Monthly cases'])
columns = (my_filtered_csv[~my_filtered_csv['date_report'].isna()])#,(my_filtered_csv[~my_filtered_csv['Monthly cases']. isna()])

x = []
y = [] 

columns = list(zip(columns['date_report'], columns['Monthly cases']))

for i in columns:
    x.append(datetime.datetime.strptime(i[0], '%Y-%m-%d').date())
    y.append(i[1])




print('Before')
print(np.corrcoef(y,y)[0][1])
print(np.corrcoef(f1,y)[0][1])
print(np.corrcoef(f2,y)[0][1])
print(np.corrcoef(f3,y)[0][1])
print(np.corrcoef(f4,y)[0][1])
print(np.corrcoef(f5,y)[0][1])

'''
f1 = np.delete(f1, index)
f2 = np.delete(f2, index)
f3 = np.delete(f3, index)
f4 = np.delete(f4, index)
f5 = np.delete(f5, index)
y = np.delete(y, -1)
'''


print('After')
print(np.corrcoef(y,y)[0][1])
print(np.corrcoef(f1,y)[0][1])
print(np.corrcoef(f2,y)[0][1])
print(np.corrcoef(f3,y)[0][1])
print(np.corrcoef(f4,y)[0][1])
print(np.corrcoef(f5,y)[0][1])





#print(y)
# split the arrays after october
y,y1 = y[0:10], y[10:]
x,x1 = x[0:10], x[10:]
f1,f12 = f1[0:10], f1[10:]
f2,f22 = f2[0:10], f2[10:] 
f3,f32= f3[0:10], f3[10:]
f4,f42 = f4[0:10],f4[10:]
f5,f52 = f5[0:10],f5[10:]

'''
print(f2)
print(f22)
print(y)

print('jan - oct ')

print(np.corrcoef(y,y)[0][1])

print(np.corrcoef(f1,y)[0][1])
print(np.corrcoef(f2,y)[0][1])
print(np.corrcoef(f3,y)[0][1])
print(np.corrcoef(f4,y)[0][1])
print(np.corrcoef(f5,y)[0][1])

print('the rest')
print(np.corrcoef(y1,y1)[0][1])
print(np.corrcoef(f12,y1)[0][1])
print(np.corrcoef(f22,y1)[0][1])
print(np.corrcoef(f32,y1)[0][1])
print(np.corrcoef(f42,y1)[0][1])
print(np.corrcoef(f52,y1)[0][1])'''
arr2 = []
arr2 = np.append(arr2, [np.corrcoef(f12,y1)[0][1],np.corrcoef(f22,y1)[0][1],np.corrcoef(f32,y1)[0][1],np.corrcoef(f42,y1)[0][1],np.corrcoef(f52,y1)[0][1]])
arr1 = []
arr1 = np.append(arr1, [np.corrcoef(f1,y)[0][1],np.corrcoef(f2,y)[0][1],np.corrcoef(f3,y)[0][1],np.corrcoef(f4,y)[0][1],np.corrcoef(f5,y)[0][1]])
while(len(y) != len(arr1)):
    arr1 = np.append(arr1, '')
while(len(y1) != len(arr2)):
    arr2 = np.append(arr2, '')
df = pd.DataFrame({"TimeSeries 1" : x, "# of Covid Cases" : y, "15 and Over": f1,"15-19": f2,"20-24": f3,"25-54": f4,"55-64": f5,"data": arr1})

df.to_csv("Timeseries 1 Eval.csv", index=False)
df =  pd.DataFrame({"TimeSeries 2" : x1, "# of Covid Cases" : y1, "15 and Over": f12,"15-19": f22,"20-24": f32,"25-54": f42,"55-64": f52, "data": arr2})
df.to_csv("Timeseries 2 Eval.csv", index=False)
print(arr1)