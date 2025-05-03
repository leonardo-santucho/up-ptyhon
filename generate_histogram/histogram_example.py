import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo
data = np.random.randn(1000)  # 1000 valores aleatorios con distribución normal

# Crear el histograma
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)

# Agregar etiquetas y título
plt.title('Histograma de ejemplo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()