import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("../data/Casos_positivos_de_COVID-19_en_Colombia.csv",encoding='utf-8-sig', sep='\s*,\s*',
                   engine='python')
grd = data.groupby(['Departamento o Distrito'])[['ID de caso']]
plt.pie(grd)
plt.show()