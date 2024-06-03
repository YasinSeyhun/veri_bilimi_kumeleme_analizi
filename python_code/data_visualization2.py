import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyası
data = pd.read_csv('customer_analysis_data.csv')


print(data.head())


gender_distribution = data['Yas'].value_counts()

# Pasta grafiği
plt.figure(figsize=(8, 8))
plt.pie(gender_distribution, labels=gender_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title('Cinsiyet Dağılımı')
plt.show()
