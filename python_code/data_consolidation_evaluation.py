import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# OMP_NUM_THREADS ayarlama
import os
os.environ["OMP_NUM_THREADS"] = "4"

# Veriyi yükleme
data = pd.read_csv("customer_analysis_data.csv")

# Sayısal değişkenleri seçme ve standardize etme
numeric_columns = ['Yas', 'Gelir', 'HarcamaMiktari', 'SatinAlmaSikligi']
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[numeric_columns])

# Elbow yöntemi ile en uygun küme sayısını belirleme
inertia = []
silhouette_scores = []
K = range(2, 11)  # 1'den başlayan küme sayıları ile hesaplamak anlamlı olmaz

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)  # n_init parametresi açıkça belirtilmiş
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_avg = silhouette_score(data_scaled, kmeans.labels_)
    silhouette_scores.append(silhouette_avg)

# Elbow grafiğini çizme
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.plot(K, inertia, 'bx-')
plt.xlabel('Küme Sayısı')
plt.ylabel('Atalet (Inertia)')
plt.title('Elbow Yöntemi ile Optimal Küme Sayısını Belirleme')

plt.subplot(1, 2, 2)
plt.plot(K, silhouette_scores, 'bx-')
plt.xlabel('Küme Sayısı')
plt.ylabel('Silhouette Skoru')
plt.title('Silhouette Yöntemi ile Optimal Küme Sayısını Belirleme')

plt.tight_layout()
plt.show()

# En uygun küme sayısını belirleyin (örneğin, 3)
optimal_k = 3

# KMeans kümeleme
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)  # n_init parametresi açıkça belirtilmiş
data['Cluster'] = kmeans.fit_predict(data_scaled)

# Orijinal veriyi küme etiketleri ile birleştirme
clustered_data = pd.concat([data, pd.DataFrame(data_scaled, columns=numeric_columns)], axis=1)

# Kategorik ve sayısal değişkenleri ayırma
categorical_columns = ['MusteriID', 'SubeID', 'Cinsiyet', 'Sehir']
numeric_columns_with_clusters = numeric_columns + ['Cluster']

# Kümeleri profil çıkarma
cluster_profiles = data[numeric_columns_with_clusters].groupby('Cluster').mean()

# Kategorik değişkenlerin her küme için dağılımını inceleme
categorical_summary = data.groupby('Cluster')[categorical_columns].agg(lambda x: x.mode()[0])

# Küme profilleri ve kategorik özetleri birleştirme
cluster_profiles = pd.concat([cluster_profiles, categorical_summary], axis=1)

print(cluster_profiles)

# Model değerlendirme metrikleri
inertia_optimal = kmeans.inertia_
silhouette_optimal = silhouette_score(data_scaled, kmeans.labels_)

print(f"Optimal Küme Sayısı: {optimal_k}")
print(f"Atalet (Inertia): {inertia_optimal}")
print(f"Silhouette Skoru: {silhouette_optimal}")
