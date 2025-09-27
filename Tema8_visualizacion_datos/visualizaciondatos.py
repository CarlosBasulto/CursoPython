# ============================================================
# TEMA 8: VISUALIZACIÓN DE DATOS EN PYTHON
# ============================================================
# Contenido:
# - Introducción a la visualización de datos
# - Librería matplotlib (gráficas estáticas rápidas)
# - Librería plotly (gráficas interactivas)
# - Ejemplos prácticos de cada tipo de gráfica
# ============================================================

# ------------------------------------------------------------
# 8.1 Introducción
# ------------------------------------------------------------
# La visualización de datos es esencial para comunicar los resultados
# de un análisis. Python ofrece muchas librerías, pero aquí veremos:
# - matplotlib: sencilla y muy usada para gráficas rápidas.
# - plotly: más moderna e interactiva.
# ------------------------------------------------------------

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ------------------------------------------------------------
# 8.2. Matplotlib
# ------------------------------------------------------------

# Ejemplo 1: Gráfica de líneas
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x, y, label="Línea simple", color="blue", marker="o")
plt.title("Gráfica de líneas (matplotlib)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()

# Ejemplo 2: Varias líneas en una misma gráfica
y2 = np.array([1, 4, 9, 16, 25])
plt.plot(x, y, label="Lineal", marker="o")
plt.plot(x, y2, label="Cuadrática", marker="s")
plt.title("Dos series de datos en una sola gráfica")
plt.legend()
plt.show()

# Ejemplo 3: Histograma
valores = np.random.randn(1000)  # 1000 valores aleatorios distribución normal
plt.hist(valores, bins=20, color="green", alpha=0.7)
plt.title("Histograma (matplotlib)")
plt.show()

# Ejemplo 4: Gráfica de barras
categorias = ["A", "B", "C"]
valores_barra = [5, 7, 3]
plt.bar(categorias, valores_barra, color=["red", "blue", "orange"])
plt.title("Gráfica de barras (matplotlib)")
plt.show()

# Ejemplo 5: Gráfico circular
partes = [30, 20, 50]
etiquetas = ["Python", "Java", "C++"]
plt.pie(partes, labels=etiquetas, autopct="%1.1f%%")
plt.title("Gráfico circular (matplotlib)")
plt.show()

# Ejemplo 6: Varias gráficas en subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4))
axs[0].plot(x, y)
axs[0].set_title("Línea")
axs[1].bar(categorias, valores_barra)
axs[1].set_title("Barras")
axs[2].hist(valores, bins=10)
axs[2].set_title("Histograma")
plt.tight_layout()
plt.show()

# Ejemplo 7: Exportar gráfica a archivo
plt.plot(x, y, color="purple")
plt.title("Ejemplo exportado")
plt.savefig("grafico_exportado.png")
plt.close()

# ------------------------------------------------------------
# 8.3. Plotly
# ------------------------------------------------------------

# Ejemplo 8: Gráfica de líneas interactiva
fig1 = go.Figure(data=go.Scatter(x=x, y=y, mode="lines+markers", name="Lineal"))
fig1.update_layout(title="Gráfica de líneas (plotly)")
fig1.show()

# Ejemplo 9: Dos series en un mismo gráfico
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Lineal"))
fig2.add_trace(go.Scatter(x=x, y=y2, mode="markers", name="Cuadrática"))
fig2.update_layout(title="Dos series (plotly)")
fig2.show()

# Ejemplo 10: Histograma
fig3 = go.Figure(data=[go.Histogram(x=valores, nbinsx=20)])
fig3.update_layout(title="Histograma (plotly)")
fig3.show()

# Ejemplo 11: Gráfica de barras
fig4 = go.Figure(data=[go.Bar(x=categorias, y=valores_barra)])
fig4.update_layout(title="Gráfica de barras (plotly)")
fig4.show()

# Ejemplo 12: Gráfico circular
fig5 = go.Figure(data=[go.Pie(labels=etiquetas, values=partes)])
fig5.update_layout(title="Gráfico circular (plotly)")
fig5.show()

# Ejemplo 13: Varias gráficas con subplots
fig6 = make_subplots(rows=1, cols=3, subplot_titles=("Línea", "Barras", "Histograma"))
fig6.add_trace(go.Scatter(x=x, y=y, mode="lines"), row=1, col=1)
fig6.add_trace(go.Bar(x=categorias, y=valores_barra), row=1, col=2)
fig6.add_trace(go.Histogram(x=valores), row=1, col=3)
fig6.update_layout(title="Subplots en plotly")
fig6.show()

# Nota: en Plotly la exportación se hace con el botón de cámara en la gráfica.
# ============================================================
# FIN DEL TEMA 8
# ============================================================
