import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

data = pd.read_csv("../data/Casos_positivos_de_COVID-19_en_Colombia.csv",encoding='utf-8-sig', sep='\s*,\s*',
                   engine='python')
data1 = len(data[(data['Estado']=='Fallecido')])
data2 = data.groupby(['Sexo','Estado']).size()
data3 = data.groupby(['Estado','Sexo']).size()
print(data2)
print(data3)
#print((data2['Estado']=='Fallecido'))
r=[0,1]
plt.bar(r[0],data3['Fallecido','F'])
plt.bar(r[0],data3['Grave','F'],bottom=data3['Fallecido','F'])
plt.bar(r[0],data3['Moderado','F'],bottom=data3['Grave','F'])
# plt.bar(r[0],data3['Leve','F'],bottom=data3['Moderado','F'])

plt.bar(r[1],data3['Fallecido','M'])
plt.bar(r[1],data3['Grave','M'],bottom=data3['Fallecido','M'])
plt.bar(r[1],data3['Moderado','M'],bottom=data3['Grave','M'])
# plt.bar(r[1],data3['Leve','M'],bottom=data3['Moderado','M'])

# plt.yticks(np.arange(0,25000,1000))
# plt.bar(data3,x='Sexo',y='Estado',color='specialization',barmode='group')
plt.show()