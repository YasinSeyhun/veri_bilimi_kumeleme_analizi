import pandas as pd
import numpy as np

# Rastgelelik için sabit bir tohum değeri belirledim.
np.random.seed(42)

# Oluşturulacak müşteri ve şube sayıları
num_customers = 1000
num_branches = 50

# Random veri seti için random methodu yardımıyla veri setinin değişkenlerini oluşturuyoruz.

# Müşteri kimlikleri
customer_ids = np.arange(1, num_customers + 1)

# Şube kimlikleri
branch_ids = np.random.choice(np.arange(1, num_branches + 1), size=num_customers)

# Yaş dağılımı
ages = np.random.randint(20, 65, size=num_customers)

# Cinsiyet dağılımı
genders = np.random.choice(['Erkek', 'Kadın'], size=num_customers)

# Gelir dağılımı (TL cinsinden)
incomes = np.random.randint(20000, 100000, size=num_customers)

# Harcama miktarı (TL cinsinden)
purchase_amounts = np.random.randint(100, 2000, size=num_customers)

# Satın alma sıklığı (yılda kaç kez)
purchase_frequencies = np.random.randint(1, 50, size=num_customers)

# Şehir bilgisi
cities = ['İstanbul', 'Ankara', 'İzmir', 'Kocaeli', 'Antalya']
customer_cities = np.random.choice(cities, size=num_customers)

# Oluşan verileri dataFrame'e yerleştiriyoruz.

# Veri setini oluştur
data = pd.DataFrame({
    'MusteriID': customer_ids,
    'SubeID': branch_ids,
    'Yas': ages,
    'Cinsiyet': genders,
    'Gelir': incomes,
    'HarcamaMiktari': purchase_amounts,
    'SatinAlmaSikligi': purchase_frequencies,
    'Sehir': customer_cities
})

# Son olarka veri setini CSV olarak kaydediyoruz.
data.to_csv('customer_analysis_data.csv', index=False)


