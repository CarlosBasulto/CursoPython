# Tema 7: Numpy y Pandas

Se introduce el análisis de datos con Python mediante **Numpy** (arrays, matrices, funciones universales, estadísticas) y **Pandas** (series, dataframes, filtrado, groupby, lectura de CSV).

**Ejemplo:**
```python
import numpy as np
import pandas as pd

arr = np.array([1,2,3])
print(arr.mean())

df = pd.DataFrame({'Nombre':['Ana','Luis'], 'Edad':[20,21]})
print(df.describe())
```

> **Nota:** Este material se usa en paralelo con las explicaciones del profesor.
