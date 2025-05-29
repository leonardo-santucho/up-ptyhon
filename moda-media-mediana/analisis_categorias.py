import pandas as pd

def cargar_y_limpiar_csv(path):
    """Carga el CSV y limpia columnas numéricas."""
    df = pd.read_csv(path)
    cols = ['Video views', 'Likes', 'Dislikes']
    for col in cols:
        df[col] = df[col].str.replace(',', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def top_categorias_por_vistas(df, top_n=3):
    """Devuelve las top N categorías con más vistas promedio."""
    if 'Category' not in df.columns:
        raise ValueError("La columna 'Category' no existe en el dataset.")
    
    resumen = (
        df.groupby('Category')['Video views']
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
    )
    return resumen

# Solo se ejecuta si corrés este script directamente
if __name__ == "__main__":
    df = cargar_y_limpiar_csv('top-1000-trending-youtube-videos.csv')
    top = top_categorias_por_vistas(df)
    print("📺 Categorías más vistas en promedio:")
    print(top)
