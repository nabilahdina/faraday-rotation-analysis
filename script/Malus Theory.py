import pandas as pd
import matplotlib.pyplot as plt

# 1. Data Percobaan
data = pd.read_csv("Theory.csv", skiprows=1)

# 2. Cek nama kolom
print(data.columns)

# 3. Ambil kolom dengan nama yang benar dan ubah koma ke titik
data['Intensitas (V)'] = data['Intensitas (V)'].astype(str).str.replace(',', '.').astype(float)
data['Sudut (°)'] = data['Sudut (°)'].astype(float)

sudut = data['Sudut (°)']           # kolom sudut (derajat)
intensitas = data['Intensitas (V)'] # kolom intensitas

# 4. Plot grafik
plt.scatter(sudut, intensitas, color='red', s=20, label='Data')  # titik data
plt.plot(sudut, intensitas, color='green', alpha=0.5)              # garis penghubung

# 5. Tambahkan judul dan label
plt.title("Grafik Hubungan antara Besar Sudut dengan Intensitas Pada Teori Malus")
plt.xlabel("Sudut (°)")
plt.ylabel("Intensitas (V)")
plt.grid(True)
plt.legend()

# 6. Tampilkan grafik
plt.show()