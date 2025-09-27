# ============================================================
# PRÁCTICA TEMA 6: Expresiones Regulares, Excepciones y Compresiones
# SOLO ENUNCIADOS (rellena tu solución debajo de cada bloque)
# ============================================================
# Instrucciones:
# - Lee el enunciado de cada ejercicio (comentarios).
# - Escribe tu solución DEBAJO del enunciado.
# - Usa print() para comprobar resultados.
# - No borres los enunciados. Añade tu código debajo.
# ============================================================

print("=== PRÁCTICA TEMA 6 — EMPIEZA AQUÍ ===\n")

# ------------------------------------------------------------------
# EJERCICIO 1 — re.search y patrones básicos
# Enunciado:
# 1) Pide (o define) una cadena de texto que contenga una fecha en formato DD/MM/AAAA.
# 2) Usa re.search con un patrón que valide ese formato (dos dígitos, barra, dos dígitos, barra, cuatro dígitos).
# 3) Si hay coincidencia, muestra la fecha encontrada; si no, muestra "No hay fecha".
# (Sugerencia de patrón: r"\b\d{2}/\d{2}/\d{4}\b")
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 2 — re.findall con grupos
# Enunciado:
# 1) Dada una cadena con varios correos, usa re.findall para extraer todos los emails válidos simples.
# 2) Muestra la lista resultante.
# 3) (Opcional) Usa paréntesis de captura para separar usuario y dominio.
# (Sugerencia: r"([\w\.-]+)@([\w\.-]+)\.(\w+)")
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 3 — re.split y re.sub con caracteres de escape
# Enunciado:
# 1) Dada una cadena con saltos de línea y tabuladores, usa re.split para dividir por espacios en blanco (incluye \n y \t).
# 2) Usa re.sub para reemplazar todos los saltos de línea por la cadena "[NL]".
# 3) Muestra los resultados.
# (Sugerencia: patrón de espacios: r"\s+")
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 4 — Metacaracteres ?, +, *, {n,m}, [], rangos
# Enunciado:
# 1) Define una cadena con números y repeticiones (p. ej. "112233333 7 12345 9999").
# 2) Con re.findall:
#    a) Extrae secuencias del dígito '3' repetido una o más veces.
#    b) Extrae grupos de exactamente 4 dígitos seguidos.
#    c) Extrae secuencias de dígitos del 1 al 3 repetidos 2 o más veces.
# 3) Muestra cada lista extraída.
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 5 — try/except/else/finally
# Enunciado:
# 1) Pide (o define) dos números y realiza una división a/b dentro de un bloque try.
# 2) Captura ZeroDivisionError y ValueError con except específicos y muestra un mensaje distinto para cada uno.
# 3) Si no hubo error, en el bloque else muestra el resultado.
# 4) En el bloque finally muestra "Operación finalizada".
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 6 — Manejo de múltiples excepciones y Exception
# Enunciado:
# 1) Crea un código que pueda generar distintos errores (índice fuera de rango, conversión inválida, etc.).
# 2) Maneja al menos dos tipos de errores concretos con except específicos.
# 3) Añade un except Exception genérico para capturar cualquier otro error y mostrar su mensaje.
# 4) Comprueba que el programa continúa ejecutándose después.
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 7 — raise (lanzar excepciones propias)
# Enunciado:
# 1) Implementa una función validar_dni(dni: str) que:
#    - Lance ValueError si el formato no coincide con 8 dígitos + una letra al final (sin separar).
#    - Devuelva True si el formato es correcto (no es necesario validar la letra real).
# 2) Llama a la función con varios ejemplos (válidos e inválidos) y maneja las excepciones en el llamador con try/except.
# (Sugerencia de patrón: r"^\d{8}[A-Za-z]$")
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 8 — List comprehensions (básico y con condición)
# Enunciado:
# 1) Genera una lista con los cuadrados de 1 a 20 usando comprensión de listas.
# 2) Genera otra lista solo con los cuadrados de los múltiplos de 3 entre 1 y 30.
# 3) Muestra ambas listas.
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 9 — Dict y Set comprehensions
# Enunciado:
# 1) Crea un diccionario por comprensión cuyas claves sean los números pares del 2 al 10
#    y sus valores, el cubo del número.
# 2) Crea un conjunto por comprensión con las primeras letras únicas (en minúscula)
#    de una lista de palabras (normaliza a minúsculas).
# 3) Muestra el diccionario y el conjunto.
# ------------------------------------------------------------------



# ------------------------------------------------------------------
# EJERCICIO 10 — Combinado: limpiar datos + validar con regex + comprensiones
# Enunciado:
# 1) Dada una lista de textos mixtos (nombres, emails, palabras sueltas), genera:
#    a) Una lista SOLO con los emails válidos (regex) usando list comprehension.
#    b) Un diccionario por comprensión con clave el email y valor True.
#    c) Un conjunto por comprensión con los dominios (parte después de @) de esos emails.
# 2) Muestra las tres estructuras.
# (Sugerencia de patrón email simple: r"^[\w\.-]+@[\w\.-]+\.\w+$")
# ------------------------------------------------------------------



print("\n=== FIN DE LA PRÁCTICA TEMA 6 — ¡A PROGRAMAR! ===")
