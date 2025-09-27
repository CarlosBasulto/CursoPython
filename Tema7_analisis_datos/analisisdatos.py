# ============================================================
# TEMA 7: ANÁLISIS DE DATOS CON NUMPY Y PANDAS
# ============================================================
# Contenido:
# 7.1 Introducción y objetivos
# 7.2 Numpy: arrays, matrices, funciones universales, estadísticas
# 7.3 Pandas: series, dataframes, gestión de datos, estadísticas
# 7.4 Lectura y escritura de ficheros CSV
# ============================================================

print("=== TEMA 7: DEMO COMPLETA ===\n")

# ------------------------------------------------------------
# 7.2. Numpy
# ------------------------------------------------------------
import numpy as np

print("--- Arrays y matrices en numpy ---")
# Crear un array (1D)
arr = np.array([1, 2, 3, 4, 5])
print("Array 1D:", arr)
print("Elemento en la posición 2:", arr[2])  # índice base 0

# Crear una matriz (2D)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz 2D:\n", matriz)
print("Elemento fila 1, col 2:", matriz[0, 1])

# Comparación rápida de operaciones con listas vs numpy
lista = list(range(1000000))
arr_np = np.arange(1000000)
# Con numpy las operaciones son mucho más rápidas y eficientes en memoria.

print("\n--- Funciones universales ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Suma:", np.add(a, b))
print("Resta:", np.subtract(a, b))
print("Multiplicación:", np.multiply(a, b))
print("División:", np.divide(b, a))
print("Potencia:", np.power(a, 2))
print("Raíz cuadrada:", np.sqrt(b))

print("\n--- Comparaciones ---")
print("a > b:", np.greater(a, b))
print("a == b:", np.equal(a, b))

print("\n--- Funciones estadísticas ---")
datos = np.array([10, 20, 30, 40, 50])
print("Mínimo:", np.amin(datos))
print("Máximo:", np.amax(datos))
print("Percentil 50:", np.percentile(datos, 50))
print("Mediana:", np.median(datos))
print("Media:", np.mean(datos))
print("Desviación estándar:", np.std(datos))
print("Varianza:", np.var(datos))

# ------------------------------------------------------------
# 7.3. Pandas
# ------------------------------------------------------------
import pandas as pd

print("\n--- Series en pandas ---")
serie = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("Serie:\n", serie)
print("Acceso por índice:", serie["b"])
print("Indices:", serie.index)
print("Valores:", serie.values)

print("\n--- DataFrames en pandas ---")
# Crear un DataFrame a partir de un diccionario
datos_dict = {
    "Nombre": ["Ana", "Luis", "Marta"],
    "Edad": [23, 30, 21],
    "Ciudad": ["Sevilla", "Madrid", "Granada"]
}
df = pd.DataFrame(datos_dict)
print("DataFrame:\n", df)

# Acceder a columna
print("Columna Edad:\n", df["Edad"])

# Agregar una nueva columna
df["Puntuación"] = [90, 85, 88]
print("DataFrame con nueva columna:\n", df)

# Eliminar una columna
del df["Ciudad"]
print("DataFrame tras eliminar columna:\n", df)

# Acceder a filas
print("Fila con loc (etiqueta):\n", df.loc[1])
print("Fila con iloc (posición):\n", df.iloc[0])

# Filtrado
print("Filtrado por Edad > 22:\n", df[df["Edad"] > 22])

# Transpuesta
print("Transpuesta:\n", df.T)

print("\n--- Gestión de datos en pandas ---")
# Ordenar por valores
print("Ordenado por Edad:\n", df.sort_values(by="Edad"))

# Agrupar por valores
df["Grupo"] = ["A", "B", "A"]
print("Agrupar por Grupo y media de Edad:\n", df.groupby("Grupo")["Edad"].mean())

# Aplicar función
df["Edad2"] = df["Edad"].apply(lambda x: x * 2)
print("Aplicando función lambda a Edad:\n", df)

print("\n--- Estadísticas en pandas ---")
print("Describe:\n", df.describe())
print("Media Edad:", df["Edad"].mean())
print("Mediana Puntuación:", df["Puntuación"].median())

# ------------------------------------------------------------
# 7.4. Lectura y escritura de CSV
# ------------------------------------------------------------
print("\n--- Lectura y escritura de CSV ---")
# Crear un DataFrame de ejemplo
df_csv = pd.DataFrame({
    "Producto": ["Mesa", "Silla", "Lámpara"],
    "Precio": [50, 20, 35],
    "Stock": [10, 50, 20]
})

# Guardar a CSV
df_csv.to_csv("productos.csv", index=False)
print("Archivo 'productos.csv' guardado.")

# Leer desde CSV
df_leido = pd.read_csv("productos.csv")
print("DataFrame leído desde CSV:\n", df_leido)

# ============================================================
# Resumen
# - numpy: arrays, matrices, operaciones universales, estadísticas.
# - pandas: series, dataframes, gestión de datos, estadísticas.
# - CSV: leer con read_csv(), guardar con to_csv().
# ============================================================

print("\n=== FIN DEL TEMA 7 — DEMO COMPLETADA ===")
