import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('customer_analysis_data.csv')

# Dağılım
sns.histplot(data['SatinAlmaSikligi'])
plt.show()

# Korelasyon
sns.scatterplot(x='Gelir', y='Sehir', data=data)
plt.show()
