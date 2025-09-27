
# Tema 7: Numpy y Pandas

En este tema se introduce el **análisis de datos con Python** mediante:

- **Numpy**: arrays, matrices, funciones universales, operaciones estadísticas.
- **Pandas**: series, dataframes, filtrado de datos, operaciones `groupby`, lectura y escritura de CSV.

Este material se usa **en paralelo con las explicaciones del profesor** y los ejemplos prácticos en clase.

---

## 🚀 Instalación de dependencias

Para poder ejecutar los ejemplos de este tema, necesitas instalar las librerías **numpy** y **pandas**.

### Usando pip
```bash
pip install numpy pandas
```

### Si usas Jupyter Notebook o Google Colab
```python
!pip install numpy pandas
```

### Verificar instalación
```python
import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)
```

---

## 📌 Ejemplo básico

```python
import numpy as np
import pandas as pd

# Crear un array de Numpy y calcular la media
arr = np.array([1, 2, 3])
print("Media del array:", arr.mean())

# Crear un DataFrame de Pandas y obtener estadísticas descriptivas
df = pd.DataFrame({'Nombre': ['Ana', 'Luis'], 'Edad': [20, 21]})
print("Resumen estadístico del DataFrame:")
print(df.describe())
```

---

## 🎯 Objetivo del tema
El objetivo es que el alumno se familiarice con las estructuras de datos de **Numpy** y **Pandas**, y aprenda a manipular, resumir y analizar datos de forma sencilla y eficiente.
