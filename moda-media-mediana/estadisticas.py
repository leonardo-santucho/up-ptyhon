import pandas as pd

# 📂 Cargar el archivo CSV (ajustá si lo moviste de carpeta)
df = pd.read_csv('top-1000-trending-youtube-videos.csv')

# 🧹 Limpiar columnas numéricas
cols_to_clean = ['Video views', 'Likes', 'Dislikes']
for col in cols_to_clean:
    df[col] = df[col].str.replace(',', '', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')  # convierte a NaN si no puede parsear

# 📊 Función para calcular media, mediana y moda
def calcular_estadisticas(col):
    media = df[col].mean()
    mediana = df[col].median()
    moda = df[col].mode().iloc[0] if not df[col].mode().empty else None
    return media, mediana, moda

# 🔁 Aplicar a cada columna y mostrar
for col in cols_to_clean:
    media, mediana, moda = calcular_estadisticas(col)
    print(f"\n📈 Estadísticas para '{col}':")
    print(f"Media: {media:,.0f}")
    print(f"Mediana: {mediana:,.0f}")
    print(f"Moda: {moda:,.0f}")
