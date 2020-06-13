import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("../data/Casos_positivos_de_COVID-19_en_Colombia.csv")

px = sns.countplot(data=data,x='Sexo', order=data.Sexo.value_counts().iloc[:2].index)
plt.show()

# /
