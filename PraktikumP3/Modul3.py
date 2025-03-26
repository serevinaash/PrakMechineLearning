# %%
import pandas as pd

# %%
# Membaca dataset
data = pd.read_csv("students.csv")

# %%
# Menampilkan 10 baris pertama
print(data.head(10))

# %%
# Menampilkan informasi dataset
data.info()

# %%
# Mengecek jumlah missing values di setiap fitur
print("\nMissing values sebelum handling:")
print(data.isna().sum())

# %%
# Mengatasi missing value pada fitur lunch dengan modus
data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)

# %%
# Mengatasi missing value pada fitur reading score dengan mean
data['reading score'].fillna(data['reading score'].mean(), inplace=True)

# %%
# Mengatasi missing value pada fitur grade dengan median
data['grade'].fillna(data['grade'].median(), inplace=True)

# %%
# Mengecek kembali apakah masih ada missing values
print("\nMissing values setelah handling:")
print(data.isna().sum())

# %%
# Menampilkan informasi dataset setelah handling missing values
data.info()

# %%
# Alternatif handling missing values

# Menggunakan teknik interpolasi
data['nama_fitur'] = data['nama_fitur'].interpolate(method='linear')

# Menggunakan teknik backward fill
data['nama_fitur'].fillna(method='bfill', inplace=True)

# Menggunakan teknik forward fill
data['nama_fitur'].fillna(method='ffill', inplace=True)

# Menggunakan teknik dropping untuk menghapus baris dengan missing value
data.dropna(axis=0, inplace=True)

# Menggunakan teknik dropping untuk menghapus fitur dengan lebih dari 50% missing value
threshold = len(data) * 0.5
data.dropna(thresh=threshold, axis=1, inplace=True)

# %%
# Menampilkan informasi dataset setelah alternatif handling missing values
data.info()
