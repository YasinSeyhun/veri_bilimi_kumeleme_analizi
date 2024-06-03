import pandas as pd


data = pd.read_csv('customer_analysis_data.csv')

# birkaç veri setini görüntülemek için
print(data.head(5))

# veri setnini genel bilgisini(info) öğrenmek için
print(data.info())

# temel istatistikleri öğrenmek için
print(data.describe())
