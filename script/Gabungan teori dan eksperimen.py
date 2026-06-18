import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Data Percobaan
data = pd.read_csv("Percobaan1.csv", skiprows=1)
data['Intensitas (V)'] = data['Intensitas (V)'].astype(str).str.replace(',', '.').astype(float)
data['Sudut (°)'] = data['Sudut (°)'].astype(float)
sudut = data['Sudut (°)']           # kolom sudut (derajat)
intensitas = data['Intensitas (V)'] # kolom intensitas

# 3. Plot data eksperimen
plt.scatter(sudut, intensitas, color='cyan', s=20, label='Data Eksperimen')
plt.plot(sudut, intensitas, color='purple', alpha=0.5)

# 4. Plot teori Malus (0° sampai 180°)
sudut_teori = np.linspace(0, 180, 200)
sudut_teori_rad = np.deg2rad(sudut_teori)
I0 = intensitas.max()
intensitas_teori = I0 * np.cos(sudut_teori_rad) ** 2

plt.plot(sudut_teori, intensitas_teori, 'r--', label='Teori Malus (I = I₀ cos²θ)')

# 5. Tambahkan judul dan label
plt.title("Grafik Hubungan Sudut vs Intensitas (Eksperimen & Teori Malus)")
plt.xlabel("Sudut (°)")
plt.ylabel("Intensitas (V)")
plt.grid(True)
plt.legend()

# 6. Tampilkan grafik
plt.show()