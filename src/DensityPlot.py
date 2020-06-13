import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("../data/Casos_positivos_de_COVID-19_en_Colombia.csv")

sns.kdeplot(data=data['Edad'],label="Edad", shade=True)
plt.show()