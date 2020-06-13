import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

data = pd.read_csv("../data/Casos_positivos_de_COVID-19_en_Colombia.csv",encoding='utf-8-sig', sep='\s*,\s*',
                   engine='python')
df1 = data[['Departamento o Distrito', 'Codigo departamento']]
grp = df1.groupby(['Departamento o Distrito', 'Codigo departamento'])
print(grp.count())