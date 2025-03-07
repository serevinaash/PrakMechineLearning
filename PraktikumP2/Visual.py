import pandas as pd
import matplotlib.pyplot as plt

# Membaca database
data = pd.read_csv("tips.csv")

# Menghitung jumlah laki-laki dan perempuan yang memberikan tips
gender_counts = data['sex'].value_counts()

# Menghitung persentase
gender_percent = (gender_counts / gender_counts.sum()) * 100

# Membuat diagram pie
plt.figure(figsize=(6, 6))
plt.pie(gender_percent, labels=gender_percent.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999', '#66b3ff'])
plt.title("Persentase Laki-laki dan Perempuan yang Memberikan Tips")
plt.show()