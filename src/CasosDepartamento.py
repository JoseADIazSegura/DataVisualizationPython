import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../data/Casos_positivos_de_COVID-19_en_Colombia.csv",encoding='utf-8-sig', sep='\s*,\s*',
                   engine='python')
grp = data.groupby(['Departamento o Distrito', 'Codigo departamento'])#.size().reset_index(name='counts')
px = sns.countplot(data=data,x='Departamento o Distrito')
px.set_xticklabels(px.get_xticklabels(),rotation=45,horizontalalignment='right')


plt.show()
print(px.get_xbound())
#print(grp.count())