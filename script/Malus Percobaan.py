import pandas as pd
import matplotlib.pyplot as plt

# Data Percobaan
data = pd.read_csv("Percobaan1.csv", skiprows=1)
print(data.columns)
data['Intensitas (V)'] = data['Intensitas (V)'].astype(str).str.replace(',', '.').astype(float)
data['Sudut (°)'] = data['Sudut (°)'].astype(float)
sudut = data['Sudut (°)']           # kolom sudut (derajat)
intensitas = data['Intensitas (V)'] # kolom intensitas

# Plot grafik
plt.scatter(sudut, intensitas, color='cyan', s=20, label='Data')  # titik data
plt.plot(sudut, intensitas, color='purple', alpha=0.5)              # garis penghubung

# Visualisasi grafik
plt.title("Grafik Hubungan antara Besar Sudut dengan Intensitas Pada Percobaan Malus")
plt.xlabel("Sudut (°)")
plt.ylabel("Intensitas (V)")
plt.grid(True)
plt.legend()
plt.show()
