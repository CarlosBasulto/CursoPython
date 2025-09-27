# ============================================================
# Tema 3: Estructuras de datos, condicionales, bucles e iteradores (Python)
# Archivo DEMO con explicaciones y ejemplos comentados
# ============================================================

print("=== DEMO TEMA 3: Estructuras de datos, condicionales, bucles e iteradores ===\n")

# 3.1. Introducción y objetivos
# Este script introduce:
# - Estructuras de datos de Python (listas, tuplas, diccionarios, conjuntos).
# - Sentencias condicionales (if, elif, else).
# - Bucles (while, for), rango range(), y else en bucles.
# - Sentencias break y continue.
# - Iteradores (iter(), next()).
# Objetivo: conocer y practicar funciones básicas para cada estructura y controlar el flujo (decisiones y repetición).


# 3.2. Estructuras de datos
# LISTAS: mutables, ordenadas, pueden mezclar tipos (aunque lo habitual es homogéneo).
# Crear listas
lista = [10, 20, 30, 40, 50]
lista_mixta = [1, "dos", 3.0, True]
lista_vacia = []
print("Lista:", lista)
print("Lista mixta:", lista_mixta)

# Acceso por índice (base 0)
primero = lista[0]           # 10
ultimo = lista[-1]           # 50 (índice negativo: desde la derecha)
sublista_0_2 = lista[0:2]    # [10, 20] (rango: inicio incluido, fin excluido)
sublista_inicio_3 = lista[:3] # [10, 20, 30]
sublista_2_final = lista[2:]  # [30, 40, 50]
print("Índice 0:", primero, "| Índice -1:", ultimo, "| Rango [0:2]:", sublista_0_2)

# Funciones/métodos frecuentes de listas
print("\n--- Métodos de listas ---")
print("len(lista) =", len(lista))             # longitud
print("lista.index(30) =", lista.index(30))   # posición de 30

lista.insert(1, 15)         # inserta 15 en la posición 1
print("insert(1,15) ->", lista)

lista.append(60)            # añade al final un elemento
print("append(60) ->", lista)

lista.extend([70, 80])      # añade varios elementos (los “extiende”)
print("extend([70,80]) ->", lista)

lista.remove(40)            # elimina la primera aparición de 40
print("remove(40) ->", lista)

print("count(20) =", lista.count(20))  # veces que aparece 20

lista.reverse()             # invierte la lista IN PLACE
print("reverse() ->", lista)

# sort requiere tipos comparables (homogéneos). Ordena in place.
lista.sort()                # creciente
print("sort() creciente ->", lista)
lista.sort(reverse=True)    # decreciente
print("sort(reverse=True) ->", lista)

# pop: quita y devuelve elemento. Sin índice, el último.
sacado = lista.pop()        # elimina el último
print("pop() ->", sacado, " | lista:", lista)
sacado_idx = lista.pop(0)   # elimina por posición
print("pop(0) ->", sacado_idx, " | lista:", lista)


# TUPLAS: como listas pero INMUTABLES
print("\n--- Tuplas ---")
tupla = (1, 2, 3, 3, 4)
print("Tupla:", tupla)
print("len(tupla) =", len(tupla))
print("tupla.count(3) =", tupla.count(3))
print("tupla.index(3) =", tupla.index(3))  # primera aparición

# Empaquetado y desempaquetado
coords = (10.5, 20.25)      # empaquetado
x, y = coords               # desempaquetado
print("coords:", coords, "| x:", x, "| y:", y)

# Acceso por índice (igual que listas, pero no se puede modificar)
print("tupla[0] =", tupla[0])


# DICCIONARIOS: pares clave-valor, claves únicas
print("\n--- Diccionarios ---")
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Sevilla"
}
print("Diccionario persona:", persona)
print("Acceso por clave persona['nombre'] ->", persona["nombre"])

# Añadir o actualizar
persona["edad"] = 29
persona["profesion"] = "Desarrolladora"
print("Tras asignaciones:", persona)

# Eliminar clave
del persona["ciudad"]
print("del persona['ciudad'] ->", persona)

# list/keys y comprobación de claves
print("list(persona) ->", list(persona))           # devuelve lista de claves
print("sorted(persona) ->", sorted(persona))       # claves ordenadas
print("'nombre' in persona ->", ("nombre" in persona))


# CONJUNTOS (set): colección NO ordenada, sin duplicados
print("\n--- Conjuntos (set) ---")
conjunto = {1, 2, 2, 3, 4, 4, 5}
print("Set sin duplicados:", conjunto)             # {1,2,3,4,5} (el orden puede variar)
conjunto_vacio = set()
conjunto.add(6)                                    # añadir un elemento
print("add(6) ->", conjunto)
print("len(conjunto) ->", len(conjunto))
print("3 in conjunto ->", (3 in conjunto))

# Operaciones de conjuntos: unión, intersección, diferencia
a = {1, 2, 3}
b = {3, 4, 5}
print("a|b (unión) ->", a | b)
print("a&b (intersección) ->", a & b)
print("a-b (diferencia) ->", a - b)

# NOTA: Al no estar ordenados, no se accede por índice (haría error).
# Ejemplo (NO ejecutar): conjunto[0]  # TypeError


# 3.3. Ejecuciones condicionales: if, elif, else
print("\n--- Condicionales ---")
numero = 7
if numero > 5:
    print("if: El número es mayor que 5.")
elif numero == 5:
    print("elif: El número es exactamente 5.")
else:
    print("else: El número es menor que o igual a 5.")


# 3.4. Ejecuciones iterativas: while y for (+ else en bucles)
print("\n--- Bucle while ---")
contador = 5
while contador >= 0:           # se repite mientras la condición sea True
    print("contador:", contador)
    contador -= 1
else:
    # En while, el else se ejecuta cuando termina el bucle “de forma natural”
    print("Fin del while (se ejecuta el else).")

print("\n--- Bucle for sobre lista ---")
numeros = [10, 20, 30]
for n in numeros:
    print("Elemento:", n)
else:
    print("Fin del for (else ejecutado).")

print("\n--- Bucle for sobre cadena ---")
mensaje = "Hola"
for ch in mensaje:
    print("Char:", ch)

print("\n--- Recorriendo por índices con range ---")
# range(inicio, fin_exclusivo, paso). Si omites inicio, empieza en 0; si omites paso, usa 1.
texto = "Hola mundo"
# Mostrar caracteres en posición par:
for i in range(0, len(texto), 2):
    print(f"i={i} -> {texto[i]}")

print("\n--- break y continue ---")
for n in range(1, 10):
    if n == 3:
        continue              # salta el 3, sigue con la siguiente iteración
    if n == 7:
        break                 # rompe el bucle al llegar a 7
    print("n:", n)
print("Tras break/continue.")


# Iteradores: iter() y next()
print("\n--- Iteradores (iter, next) ---")
lista_iterable = ["a", "b", "c"]
it = iter(lista_iterable)          # crea un iterador
print("next(it) ->", next(it))     # 'a'
print("next(it) ->", next(it))     # 'b'
print("next(it) ->", next(it))     # 'c'

# Manejo de fin de iteración:
it2 = iter("OK")
try:
    print("next(it2) ->", next(it2))   # 'O'
    print("next(it2) ->", next(it2))   # 'K'
    print("next(it2) ->", next(it2))   # StopIteration
except StopIteration:
    print("StopIteration capturada: no hay más elementos.")

# Ejemplo práctico: convertir iterador en lista para “consumir” todo
it3 = iter(range(3))                # 0,1,2
resto = list(it3)                   # ['consume' el iterador]
print("Consumido con list(it3) ->", resto)


# Referencias (documentación oficial y tutoriales; solo informativas)
# - Data structures: https://docs.python.org/3/tutorial/datastructures.html
# - Control flow (if/for/while/range): https://docs.python.org/3/tutorial/controlflow.html
# - Iteradores: https://www.w3schools.com/python/python_iterators.asp

print("\n=== FIN DE LA DEMO ===")
