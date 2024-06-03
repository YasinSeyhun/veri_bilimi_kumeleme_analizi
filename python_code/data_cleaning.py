
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('customer_analysis_data.csv')

# Eksik verileri kontrol etme ve düzeltme
print(data.isnull().sum())

# Hata ayıklayacağım sütunları seçme
features = data[['Yas', 'Gelir', 'HarcamaMiktari', 'SatinAlmaSikligi']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Ölçeklendirilmiş veriyi DataFrame'e dönüştürme
scaled_data = pd.DataFrame(scaled_features, columns=features.columns)

print(scaled_data.head())
