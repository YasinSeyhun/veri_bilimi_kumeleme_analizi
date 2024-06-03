import pandas as pd

data = pd.read_csv('customer_analysis_data.csv')

features = data[['Yas', 'Gelir', 'HarcamaMiktari', 'SatinAlmaSikligi']]

# Temel istatistikler
print(data.describe())

# Özellikler arasındaki korelasyon
# corr fonksiyonu kategorik verileri ilişkilendirmez
correlation_matrix = features.corr()
print(correlation_matrix)
