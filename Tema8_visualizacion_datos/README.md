# Tema 8: Visualización de datos (matplotlib y plotly)

Se trabajan las librerías **matplotlib** y **plotly** para generar gráficos estáticos y dinámicos. Se ven líneas, histogramas, barras, circulares, subplots y exportación de gráficos.

**Ejemplo:**
```python
import matplotlib.pyplot as plt
plt.plot([1,2,3],[2,4,6])
plt.show()

import plotly.graph_objects as go
fig = go.Figure(data=go.Scatter(y=[2,4,6]))
fig.show()
```

> **Nota:** Este tema es práctico y se explica con ejemplos en clase.
