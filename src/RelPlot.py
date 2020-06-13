import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("../data/hospital_beds_global_v1.csv")

sns.relplot(data=data,y='beds',x='year',hue='type')
plt.show()