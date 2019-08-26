import csv
import pandas as pd 
import numpy as np 
import seaborn as sb
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d


# df = pd.read_csv('Persentase_Perokok.csv')
# print(df)

# sb.relplot(x='Provinsi', y='2015', data=df)
# sb.barplot(x='Provinsi', y='2015', data=df)
# plt.grid(True)
# plt.show()
df = []
with open ('Persentase Perokok RI.csv','r') as data:
    reader = csv.DictReader(data)
    for item in reader:
        df.append(dict(item))

provinsi = []
th15 = []
th16 = []
for item in df:
    provinsi.append(item)
    th15.append(float(item['2015']))
    th16.append(float(item['2016']))
# untuk bikin jarak antar diagram. jarak 2015 = 2016 sama, ambil salah satu
x1 = np.arange(len(th15))

x = []
for loop in range (len(provinsi)):
    x.append(loop)
y1=np.repeat(1, len(th15))
y2=np.repeat(3, len(th15))

xx = []
for loop in range(0,len(provinsi)):
    xx.append(loop)

xxx = []
for loop in range (10,len(provinsi)+10):
    xxx.append(loop)

z = np.zeros(len(provinsi))
dx = np.zeros(len(provinsi))
dy = np.ones(len(provinsi))

ax = plt.subplot(111, projection='3d')
ax.bar3d(x,y1,z,dx,dy,th15,color='red')
ax.bar3d(xx,y2,z,dx,dy,th16,color='lightblue')

plt.xticks(x1, provinsi)
plt.yticks([1.5,3.5],[2015,2016])
plt.xticks(rotation=90)
plt.show()