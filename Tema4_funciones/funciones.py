# ============================================================
# TEMA 4: FUNCIONES EN PYTHON — Código DEMO comentado
# ============================================================
# Contenido:
# 4.1. Introducción y objetivos
# 4.2. Definición de funciones (def, parámetros, return)
# 4.3. Parámetros: por posición, por nombre, valores por defecto
# 4.4. Parámetros indeterminados: *args, **kwargs (mezclas)
# 4.5. Retorno de valores (uno y varios), desempaquetado
# 4.6. Documentación de funciones (docstrings, help, __doc__)
# 4.7. Funciones y módulos “built-in” y de la librería estándar (math, sys, os, random)
# 4.8. Funciones anónimas (lambda) + map/filter
# ------------------------------------------------------------

print("=== TEMA 4: FUNCIONES EN PYTHON — DEMO ===\n")

# ------------------------------------------------------------
# 4.1. Introducción y objetivos (comentario)
# ------------------------------------------------------------
# - Reutilizar código: empaquetar una tarea en una función y llamarla varias veces.
# - Organizar el programa en “bloques” con entradas (parámetros) y salidas (return).
# - Aprovechar funciones existentes de Python y su librería estándar.


# ------------------------------------------------------------
# 4.2. Definición de funciones
# Sintaxis:
#   def nombre_funcion(param1, param2, ...):
#       # cuerpo con sangría (4 espacios)
#       return resultado  # (opcional)
# ------------------------------------------------------------

def area_triangulo(base, altura):
    """Calcula el área de un triángulo con base y altura.

    Fórmula: (base * altura) / 2
    Parámetros:
      base (float|int), altura (float|int)
    Retorna:
      float: área
    """
    return (base * altura) / 2

# Llamada por posición
print("Área (posición):", area_triangulo(6, 5))

# Llamada por nombre (keyword arguments)
print("Área (nombre):", area_triangulo(base=3, altura=4))


# ------------------------------------------------------------
# 4.3. Parámetros: por posición, por nombre, valores por defecto
# - Por posición: argumentos en el mismo orden que los parámetros.
# - Por nombre: especificando param=valor (el orden ya no importa).
# - Valores por defecto: param=valor_defecto en la firma.
# ------------------------------------------------------------

def saludo(nombre="Anónimo", idioma="es"):
    """Devuelve un saludo en el idioma indicado (es/en)."""
    if idioma == "es":
        return f"Hola, {nombre}"
    elif idioma == "en":
        return f"Hello, {nombre}"
    else:
        return f"(?) {nombre}"

print("Saludo (defecto):", saludo())
print("Saludo (posición):", saludo("Carlos", "en"))
print("Saludo (nombre):", saludo(idioma="es", nombre="Lucía"))


# ------------------------------------------------------------
# 4.4. Parámetros indeterminados (*args, **kwargs)
# - *args: número variable de argumentos por posición (tupla).
# - **kwargs: número variable de argumentos por nombre (dict).
# ------------------------------------------------------------

def sumar_todo(*numeros):
    """Suma cualquier cantidad de números (por posición)."""
    total = 0
    for n in numeros:
        total += n
    return total

print("sumar_todo(1,2,3,4) ->", sumar_todo(1, 2, 3, 4))

def construir_perfil(usuario, **atributos):
    """Construye un perfil con un identificador y atributos variables."""
    perfil = {"usuario": usuario}
    perfil.update(atributos)
    return perfil

print("Perfil dinámico:", construir_perfil("ana", rol="admin", activo=True, puntos=120))

# Combinación (orden recomendado en la firma):
#   def f(param_pos, *args, param_kw=..., **kwargs): ...


# ------------------------------------------------------------
# 4.5. Retorno de valores: uno y varios
# - return x      -> devuelve un valor
# - return a, b   -> devuelve una tupla (a, b)
# - El código después de return no se ejecuta.
# ------------------------------------------------------------

def potencia(base, exponente):
    """Devuelve base ** exponente."""
    return base ** exponente

print("potencia(2, 5) ->", potencia(2, 5))

def estadisticas_basicas(nums):
    """Devuelve varias métricas a la vez: (min, max, promedio)."""
    minimo = min(nums)
    maximo = max(nums)
    promedio = sum(nums) / len(nums) if nums else 0
    return minimo, maximo, promedio  # <- tupla

datos = [10, 3, 25, 7, 7, 18]
mn, mx, avg = estadisticas_basicas(datos)  # desempaquetado
print(f"Estadísticas -> min={mn}, max={mx}, media={avg:.2f}")


# ------------------------------------------------------------
# 4.6. Documentar funciones: docstrings + help
# - El docstring es una cadena justo después de la cabecera def.
# - Se accede con __doc__ o con help(funcion).
# ------------------------------------------------------------

def convertir_celsius_a_fahrenheit(c):
    """Convierte grados Celsius a Fahrenheit.

    Fórmula: F = C * 9/5 + 32
    Parámetros:
      c (float|int): grados Celsius
    Retorna:
      float: grados Fahrenheit
    """
    return c * 9/5 + 32

print("\nDocstring de convertir_celsius_a_fahrenheit:")
print(convertir_celsius_a_fahrenheit.__doc__)

# También podrías usar help(convertir_celsius_a_fahrenheit)
# (suele imprimir mucho en consola):
# help(convertir_celsius_a_fahrenheit)


# ------------------------------------------------------------
# 4.7. Funciones y módulos de la librería estándar
# - math: funciones matemáticas
# - sys: información del intérprete, argv, etc.
# - os / os.path: sistema de ficheros
# - random: aleatoriedad
# ------------------------------------------------------------
import math
import sys
import os
import random

print("\n--- Módulo math ---")
print("fabs(-3.7) ->", math.fabs(-3.7))          # valor absoluto (float)
print("gcd(40, 28) ->", math.gcd(40, 28))        # máximo común divisor
print("floor(3.99) ->", math.floor(3.99))        # entero <= x
print("ceil(3.01)  ->", math.ceil(3.01))         # entero >= x
print("factorial(5) ->", math.factorial(5))      # 120
print("trunc(5.99)  ->", math.trunc(5.99))       # 5
print("sin(pi/2)    ->", math.sin(math.pi/2))    # 1.0
print("hypot(3,4)   ->", math.hypot(3, 4))       # 5.0
print("log(8, 2)    ->", math.log(8, 2))         # 3.0
print("log2(8)      ->", math.log2(8))           # 3.0
print("log10(1000)  ->", math.log10(1000))       # 3.0
print("pow(2, 10)   ->", math.pow(2, 10))        # 1024.0
print("sqrt(81)     ->", math.sqrt(81))          # 9.0
print("Constantes: pi =", math.pi, "| e =", math.e)

print("\n--- Módulo sys ---")
print("sys.version   ->", sys.version.split()[0])     # versión corta
print("sys.executable->", sys.executable)             # ruta del ejecutable de Python
print("sys.platform  ->", sys.platform)               # plataforma
print("sys.argv      ->", sys.argv)                    # argumentos de línea de comandos (si los hay)
# Simulación de tratamiento de argv (para clase):
if len(sys.argv) > 1:
    print("Argumentos recibidos (sin script):", sys.argv[1:])

print("\n--- Módulo os / os.path ---")
# Directorio actual
cwd = os.getcwd()
print("Directorio actual:", cwd)

# Crear y eliminar un directorio de demo (seguro)
demo_dir = os.path.join(cwd, "demo_tmp_dir")
if not os.path.exists(demo_dir):
    os.mkdir(demo_dir)
    print("mkdir:", demo_dir, "-> creado")

print("exists(demo_dir) ->", os.path.exists(demo_dir))
print("isdir(demo_dir)  ->", os.path.isdir(demo_dir))

# Crear un archivo de prueba dentro del directorio y luego eliminarlo
demo_file = os.path.join(demo_dir, "demo_tmp.txt")
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("Archivo temporal de ejemplo.\n")

print("isfile(demo_file) ->", os.path.isfile(demo_file))
print("abspath(demo_file)->", os.path.abspath(demo_file))
print("basename(demo_file)->", os.path.basename(demo_file))

# Limpieza de la demo (eliminar archivo y carpeta)
os.remove(demo_file)
os.rmdir(demo_dir)
print("remove/rmdir -> demo limpiado correctamente")

print("\n--- Módulo random ---")
nums = list(range(1, 11))
print("randint(1,10) ->", random.randint(1, 10))     # entero aleatorio
print("choice(nums)  ->", random.choice(nums))        # un elemento aleatorio
copia = nums[:]                                      # copia para mezclar
random.shuffle(copia)                                 # mezcla in-place
print("shuffle(nums) ->", copia)
print("sample(nums, 3) ->", random.sample(nums, 3))   # 3 elementos únicos aleatorios


# ------------------------------------------------------------
# 4.8. Funciones anónimas (lambda) y su uso con map/filter
# - lambda argumentos: expresión
# - map(func, secuencia) -> aplica la función a cada elemento
# - filter(func_cond, secuencia) -> mantiene los elementos donde func_cond(elem) es True
# ------------------------------------------------------------

# Función normal vs función lambda (cuadrado)
def cuadrado(x):
    """Devuelve el cuadrado de x."""
    return x ** 2

cuadrado_lambda = lambda x: x ** 2  # misma lógica, forma compacta (una sola expresión)

print("\ncuadrado(7) ->", cuadrado(7))
print("lambda cuadrado(7) ->", cuadrado_lambda(7))

# Usando map con lambda
valores = [1, 2, 3, 4, 5]
dobles = list(map(lambda n: n * 2, valores))
print("map(lambda n: n*2, valores) ->", dobles)

# Usando filter con lambda (pares)
pares = list(filter(lambda n: n % 2 == 0, valores))
print("filter(lambda n: n%2==0, valores) ->", pares)

# Combinando map + filter: cuadrados de los impares
cuadrados_impares = list(map(lambda n: n ** 2, filter(lambda n: n % 2 != 0, valores)))
print("Cuadrados de impares ->", cuadrados_impares)


# ------------------------------------------------------------
# Resumen rápido (comentarios):
# - def …: define funciones con parámetros y opcionalmente return.
# - Parámetros por posición y por nombre (keyword). Valores por defecto.
# - *args / **kwargs para argumentos variables.
# - return puede devolver varios valores (tupla) y desempaquetarse.
# - Docstrings ("""…""") para documentar: __doc__ y help().
# - math/sys/os/random: módulos estándar muy útiles.
# - lambda: funciones anónimas (una expresión). Útiles con map/filter.
# ------------------------------------------------------------

print("\n=== FIN DEL TEMA 4 — DEMO COMPLETADA ===")
