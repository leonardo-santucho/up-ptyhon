import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar CSV
df = pd.read_csv('top-1000-trending-youtube-videos.csv')

# Limpiar y convertir a numérico
cols = ['Video views', 'Likes', 'Dislikes']
for col in cols:
    df[col] = df[col].str.replace(',', '', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Configuración general de gráficos
sns.set(style='whitegrid')
plt.figure(figsize=(16, 12))

# 🔢 Histograma
for i, col in enumerate(cols, 1):
    plt.subplot(3, 2, i * 2 - 1)
    sns.histplot(df[col].dropna(), kde=True, bins=40)
    plt.title(f'Histograma: {col}')
    plt.xlabel(col)
    plt.ylabel('Frecuencia')

# 📦 Boxplot
    plt.subplot(3, 2, i * 2)
    sns.boxplot(x=df[col].dropna())
    plt.title(f'Boxplot: {col}')
    plt.xlabel(col)

plt.tight_layout()
plt.show()
