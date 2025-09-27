# Sandbox para practicar escribiendo --> no copiando. Lo iremos haciendo en clase

# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

import plotly.graph_objects as go
from plotly.subplots import make_subplots
# Ejemplo 13: Varias gráficas con subplots
fig6 = make_subplots(rows=1, cols=3, subplot_titles=("Línea", "Barras", "Histograma"))
fig6.add_trace(go.Scatter(x=x, y=y, mode="lines"), row=1, col=1)
fig6.add_trace(go.Bar(x=categorias, y=valores_barra), row=1, col=2)
fig6.add_trace(go.Histogram(x=valores), row=1, col=3)
fig6.update_layout(title="Subplots en plotly")
fig6.show()