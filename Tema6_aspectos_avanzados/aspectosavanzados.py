# ============================================================
# TEMA 6: EXPRESIONES REGULARES, ERRORES Y COMPRESIÓN DE LISTAS
# ============================================================
# Contenido:
# 6.1 Introducción y objetivos
# 6.2 Expresiones regulares
# 6.3 Errores y excepciones
# 6.4 Compresión de listas
# ============================================================

print("=== TEMA 6: DEMO COMPLETA ===\n")

# ------------------------------------------------------------
# 6.2. Expresiones regulares
# ------------------------------------------------------------
# Para trabajar con expresiones regulares usamos el módulo "re"
import re

texto = "Mi número de teléfono es 654-123-987 y mi correo es ejemplo@test.com"

# search(): busca la primera aparición de un patrón
patron = r"\d{3}-\d{3}-\d{3}"  # busca un teléfono con formato 123-456-789
resultado = re.search(patron, texto)
print("search():", resultado.group() if resultado else "No encontrado")

# match(): busca solo al principio de la cadena
resultado = re.match(r"Mi número", texto)
print("match():", "Coincidencia encontrada" if resultado else "No coincide")

# findall(): devuelve todas las coincidencias
resultado = re.findall(r"\w+@\w+\.\w+", texto)
print("findall():", resultado)

# split(): divide el texto por un patrón
resultado = re.split(r"\s", texto)  # divide por espacios
print("split():", resultado)

# sub(): sustituye patrones encontrados
resultado = re.sub(r"\d", "#", texto)
print("sub():", resultado)

# Ejemplo con metacaracteres
texto2 = "La secuencia 333 y 123 y 12222 aparecen aquí."
print("Patrón con + :", re.findall(r"3+", texto2))   # 3 repetido una o más veces
print("Patrón con {2,3} :", re.findall(r"\d{2,3}", texto2))  # números de 2 o 3 dígitos


# ------------------------------------------------------------
# 6.3. Errores y excepciones
# ------------------------------------------------------------
print("\n--- Errores y excepciones ---")

# Ejemplo de error normal (descomentar para ver fallo):
# print("Hola" + 5)   # TypeError

# Ejemplo con try-except
try:
    lista = [1, 2, 3]
    print(lista[5])  # Accedemos a índice inexistente
except IndexError:
    print("Error: El índice no existe.")
finally:
    print("Bloque finally siempre se ejecuta.")

print("El programa sigue ejecutándose.\n")

# Varios except
try:
    x = int("texto")  # esto produce ValueError
except ValueError:
    print("Error: No se puede convertir texto a entero.")
except Exception as e:
    print("Otro error:", e)

# Bloque else (cuando no hay errores)
try:
    lista = [10, 20, 30]
    print("Elemento en posición 1:", lista[1])
except IndexError:
    print("Índice fuera de rango.")
else:
    print("Acceso correcto, no hubo errores.")

# Lanzar un error manualmente
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as e:
    print("Excepción lanzada:", e)


# ------------------------------------------------------------
# 6.4. Compresión de listas
# ------------------------------------------------------------
print("\n--- Compresión de listas ---")

# Lista de cuadrados de 1 a 10 usando for
cuadrados = []
for i in range(1, 11):
    cuadrados.append(i ** 2)
print("Cuadrados con for:", cuadrados)

# Lista de cuadrados de 1 a 10 con comprensión de listas
cuadrados_comp = [i**2 for i in range(1, 11)]
print("Cuadrados con compresión:", cuadrados_comp)

# Con condición: solo múltiplos de 3
multiplos_3 = [i**2 for i in range(1, 11) if i % 3 == 0]
print("Cuadrados múltiplos de 3:", multiplos_3)

# Diccionarios por compresión: clave=número, valor=su cuadrado (solo pares)
dicc = {i: i**2 for i in range(1, 11) if i % 2 == 0}
print("Diccionario cuadrados pares:", dicc)

# Conjuntos por compresión
conj = {i**2 for i in range(1, 11) if i % 2 != 0}
print("Conjunto cuadrados impares:", conj)

# Ejemplo combinado: emails válidos de una lista de textos
correos = ["juan@test.com", "maria123@correo.es", "dato_invalido", "otro@mail.net"]
validos = [c for c in correos if re.match(r"\w+@\w+\.\w+", c)]
print("Correos válidos:", validos)


# ============================================================
# Resumen
# - Expresiones regulares: permiten buscar y manipular texto con patrones.
# - Errores y excepciones: try, except, else, finally, raise.
# - Compresión de listas: crear listas, diccionarios y conjuntos en una sola línea.
# ============================================================

print("\n=== FIN DEL TEMA 6 — DEMO COMPLETADA ===")
