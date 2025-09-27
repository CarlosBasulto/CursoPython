# ============================================================
# PRÁCTICA TEMA 7: NumPy y Pandas — SOLO ENUNCIADOS
# ============================================================
# Instrucciones:
# - Este archivo contiene 10 ejercicios. Cada uno está descrito SOLO como comentarios.
# - Escribe tu solución DEBAJO del enunciado correspondiente.
# - Usa print() para comprobar resultados y type() cuando tenga sentido.
# - No borres los enunciados. Añade tu código debajo.
# - Puedes crear archivos CSV de prueba cuando se pida (usa to_csv) y luego léelos.
# ============================================================

print("=== PRÁCTICA TEMA 7 — EMPIEZA AQUÍ ===\n")

# (Puedes dejar estos imports aquí para todos los ejercicios)
import numpy as np
import pandas as pd

# ------------------------------------------------------------
# EJERCICIO 1 — Arrays 1D y 2D (básicos)
# Enunciado:
# 1) Crea un array 1D con los enteros del 1 al 5 (np.array o np.arange).
# 2) Muestra: el primer elemento, el último, y el “slice” de los 3 primeros.
# 3) Crea una matriz 2D de shape (2,3) con números del 1 al 6.
# 4) Muestra el elemento de la fila 2, columna 3 (índices base 0) y la 1ª fila completa.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 2 — UFuncs aritméticas y broadcasting
# Enunciado:
# 1) Crea dos arrays 1D de igual longitud (por ej. [1,2,3] y [4,5,6]).
# 2) Aplica: np.add, np.subtract, np.multiply, np.divide, np.power, np.sqrt (cuando aplique).
# 3) Muestra un ejemplo de broadcasting sumando un escalar a todo el array.
# 4) Explica en un comentario qué es el broadcasting.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 3 — Comparaciones y enmascarado booleano
# Enunciado:
# 1) Con un array 1D de enteros, calcula máscaras booleanas con np.greater, np.equal, etc.
# 2) Usa una máscara para filtrar y quedarte SOLO con los valores > que la media del array.
# 3) Muestra la máscara y el resultado filtrado.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 4 — Estadística en NumPy (1D y por ejes)
# Enunciado:
# 1) Crea un array 1D con números (al menos 8 valores).
# 2) Calcula: np.amin, np.amax, np.percentile(…,50), np.median, np.mean, np.std, np.var.
# 3) Crea una matriz 2D y calcula min, max y mean por filas (axis=1) y por columnas (axis=0).
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 5 — Broadcasting con 2D (vector + matriz)
# Enunciado:
# 1) Crea una matriz 2D de shape (3,3).
# 2) Crea un vector 1D de longitud 3 (por ejemplo, [10,20,30]).
# 3) Súmalos usando broadcasting para sumar el vector a cada fila de la matriz.
# 4) Repite (si quieres) el caso sumando el vector por columnas (usa reshape si es necesario).
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 6 — Series en Pandas
# Enunciado:
# 1) Crea una pd.Series con valores [10,20,30] y un índice personalizado ['a','b','c'].
# 2) Accede por etiqueta ('b') y por posición (iloc).
# 3) Muestra .index y .values.
# 4) Crea otra Series con mismo índice y súmalas; comenta qué pasa si los índices no coinciden.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 7 — DataFrame: creación, columnas y selección
# Enunciado:
# 1) Crea un DataFrame desde un diccionario con columnas: Nombre, Edad, Ciudad (3 filas).
# 2) Añade una columna nueva “Puntuacion” (lista de 3 números).
# 3) Elimina la columna “Ciudad”.
# 4) Selecciona una fila por etiqueta (.loc) y otra por posición (.iloc).
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 8 — Filtrado, ordenación y operaciones columna
# Enunciado:
# 1) Filtra el DataFrame anterior para quedarte con Edad > 25.
# 2) Ordena por la columna “Puntuacion” descendente (sort_values).
# 3) Crea una nueva columna “Edad2” aplicando una función (lambda) que duplique la edad (apply).
# 4) Ordena por índice (sort_index) y comenta la diferencia con sort_values.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 9 — GroupBy y estadísticas en DataFrame
# Enunciado:
# 1) Añade una columna “Grupo” (por ejemplo con valores ['A','B','A']).
# 2) Agrupa por “Grupo” y calcula: tamaño de cada grupo (count) y media de “Puntuacion”.
# 3) Muestra el resultado del groupby; opcional: reinicia índice (reset_index).
# 4) Llama a .describe() sobre el DataFrame y comenta 2 métricas que te resulten útiles.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 10 — CSV: escritura, lectura y limpieza básica
# Enunciado:
# 1) Crea un DataFrame con 4-5 filas y algunas columnas (incluye al menos una con NaN).
# 2) Guarda a CSV (to_csv) sin índice, con nombre “datos_alumnos.csv”.
# 3) Lee el CSV con pd.read_csv y comprueba tipos de datos (dtypes).
# 4) Realiza una limpieza simple: rellena NaN de una columna con fillna o elimina filas con dropna.
# 5) (Opcional) Usa sep=';' al guardar y vuelve a leer indicando el separador.
# ------------------------------------------------------------



print("\n=== FIN DE LA PRÁCTICA TEMA 7 — ¡A PROGRAMAR! ===")
