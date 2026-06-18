import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Data Verdet
data = pd.read_csv("Verdet.csv", skiprows=1)
data.columns = data.columns.str.strip()
data['B (T)'] = data['B (T)'].astype(str).str.replace(',', '.').astype(float)
data['Δθ'] = data['Δθ'].astype(str).str.replace(',', '.').astype(float)

# Physical Parameters
X = data['B (T)'].values.reshape(-1, 1)  # Sumbu-x: B
y = data['Δθ'].values                    # Sumbu-y: Δθ

# Regresi linear
reg = LinearRegression().fit(X, y)
m = reg.coef_[0]
c = reg.intercept_
r2 = reg.score(X, y)

# konstanta Verdet (L = 10 cm = 0.1 m)
L = 0.1
V = m / L

# Plot data dan regresi
plt.scatter(X, y, color='magenta', label='Data (Titik)')
plt.plot(X, y, color='blue', alpha=0.5, label='Data (Garis)')  # Data tersambung garis
x_line = np.linspace(X.min(), X.max(), 100)
y_line = reg.predict(x_line.reshape(-1, 1))
plt.plot(x_line, y_line, 'r-', label=f'Regresi Linear: Δθ = {m:.3f}·B + {c:.3f}')


persamaan = f"Δθ = {m:.3f}·B + {c:.3f}\n$R^2$ = {r2:.4f}"
plt.annotate(persamaan, xy=(0.05, 0.95), xycoords='axes fraction',
             fontsize=10, backgroundcolor='white', verticalalignment='top')

plt.xlabel('Medan Magnet B (T)')
plt.ylabel('Perubahan Sudut Δθ (derajat)')
plt.title('Grafik Konstanta Verdet')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Gradien (slope, m)      = {m:.6f}")
print(f"Intercept (c)           = {c:.6f}")
print(f"R^2                     = {r2:.6f}")
print(f"Konstanta Verdet (V)    = {V:.6f} derajat/T/m")
print(f"Persamaan regresi: Δθ = {m:.3f}·B + {c:.3f}")