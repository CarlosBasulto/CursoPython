# ============================================================
# TEMA 5: ORGANIZACIÓN DEL CÓDIGO Y POO EN PYTHON — DEMO
# ============================================================
# Contenido:
# 5.1. Introducción y objetivos
# 5.2. Módulos y paquetes (qué son, cómo crearlos, cómo usarlos)
# 5.3. Programación orientada a objetos (clases, atributos, métodos, herencia)
# ------------------------------------------------------------

print("=== TEMA 5: ORGANIZACIÓN DEL CÓDIGO Y POO EN PYTHON ===\n")

# ------------------------------------------------------------
# 5.1. Introducción y objetivos
# ------------------------------------------------------------
# - Organizar proyectos grandes con módulos y paquetes.
# - Importar código de forma modular.
# - Usar programación orientada a objetos (POO).
# - Documentar funciones, módulos y clases.
# - Usar herencia para reutilizar código en clases.


# ------------------------------------------------------------
# 5.2. Módulos y paquetes
# ------------------------------------------------------------
# ➤ Módulo: un archivo .py que contiene funciones, variables o clases.
# ➤ Paquete: carpeta con varios módulos y un archivo __init__.py.
#
# Ejemplo de módulo: circunferencia.py
# Contenido:
"""
# circunferencia.py
import math

def perimetro(radio):
    return 2 * math.pi * radio

def area(radio):
    return math.pi * radio ** 2
"""
# Para usarlo desde otro archivo:
# import circunferencia
# print(circunferencia.perimetro(5))
# print(circunferencia.area(5))

# Podemos asignar alias al importar:
# import circunferencia as circ
# print(circ.area(10))

# Ejemplo de paquete:
# figuras/
#   __init__.py
#   circunferencia.py
#   poligono.py
#
# En __init__.py podríamos incluir:
"""
from .circunferencia import *
from .poligono import *
"""
# Para usarlo:
# import figuras
# print(figuras.area_circulo(5))

# Documentar módulos:
"""
\"\"\" 
Este módulo permite calcular áreas y perímetros de circunferencias.
Funciones:
- perimetro(radio): devuelve el perímetro.
- area(radio): devuelve el área.
\"\"\"
"""

print("--- Ejemplo módulo circunferencia importado como demo ---")
import math

def perimetro_demo(radio):
    """Perímetro de una circunferencia con radio r."""
    return 2 * math.pi * radio

def area_demo(radio):
    """Área de una circunferencia con radio r."""
    return math.pi * radio**2

print("Perímetro radio=5 ->", perimetro_demo(5))
print("Área radio=5 ->", area_demo(5))


# ------------------------------------------------------------
# 5.3. Programación Orientada a Objetos
# ------------------------------------------------------------
# - class: define la estructura de un objeto.
# - atributos: características (datos).
# - métodos: comportamientos (funciones dentro de la clase).
# - self: referencia al propio objeto.
# - __init__: método especial que actúa como constructor.
# - Herencia: clases hijas que extienden el comportamiento de la clase padre.


# Ejemplo 1: Clase Libro
print("\n--- Clase Libro ---")

class Libro:
    """Representa un libro con título, autor e ISBN."""

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = None
        self.paginas = 0
        self.edicion = 1

    def descripcion(self):
        """Muestra información básica del libro."""
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn})"

    def cambiar_editorial(self, nueva_editorial):
        """Cambia la editorial del libro."""
        self.editorial = nueva_editorial

# Crear un libro
mi_libro = Libro("1984", "George Orwell", "1234567890")
print(mi_libro.descripcion())
mi_libro.cambiar_editorial("Secker & Warburg")
print("Editorial:", mi_libro.editorial)


# Ejemplo 2: Herencia con clases Persona, Alumno, Profesor
print("\n--- Herencia: Persona, Alumno, Profesor ---")

class Persona:
    """Clase base para personas (atributos comunes)."""
    def __init__(self, nombre, nacimiento, domicilio):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.domicilio = domicilio

    def cambiar_domicilio(self, nuevo_domicilio):
        self.domicilio = nuevo_domicilio

    def __str__(self):
        return f"{self.nombre}, nacido en {self.nacimiento}, vive en {self.domicilio}"

class Alumno(Persona):
    """Clase Alumno que hereda de Persona."""
    def __init__(self, nombre, nacimiento, domicilio, asignatura):
        super().__init__(nombre, nacimiento, domicilio)
        self.asignatura = asignatura
        self.calificacion = None

    def poner_calificacion(self, nota):
        self.calificacion = nota

class Profesor(Persona):
    """Clase Profesor que hereda de Persona."""
    def __init__(self, nombre, nacimiento, domicilio, especialidad):
        super().__init__(nombre, nacimiento, domicilio)
        self.especialidad = especialidad
        self.asignaturas_impartidas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas_impartidas.append(asignatura)

# Crear objetos de Alumno y Profesor
alumno1 = Alumno("Carlos", "2000-05-12", "Sevilla", "Matemáticas")
profesor1 = Profesor("Ana", "1980-09-22", "Madrid", "Física")

print(alumno1)   # Usa __str__ heredado
alumno1.poner_calificacion(9)
print("Calificación:", alumno1.calificacion)

print(profesor1)
profesor1.agregar_asignatura("Álgebra")
print("Asignaturas impartidas:", profesor1.asignaturas_impartidas)

# Mostrar que heredan métodos de Persona
alumno1.cambiar_domicilio("Granada")
print("Nuevo domicilio alumno:", alumno1.domicilio)


# ------------------------------------------------------------
# Documentar clases
# ------------------------------------------------------------
# Igual que con funciones, podemos usar docstrings.
# Ejemplo:
print("\n--- Documentación de la clase Persona ---")
print(Persona.__doc__)
help(Persona)

# ------------------------------------------------------------
# Resumen rápido (comentarios):
# - Módulos: archivos .py que agrupan funciones y clases.
# - Paquetes: carpetas con __init__.py que agrupan módulos.
# - POO en Python: class, atributos, métodos, __init__, self.
# - Herencia: super() permite heredar y extender clases.
# - Documentación: docstrings en módulos, funciones y clases.
# ------------------------------------------------------------

print("\n=== FIN DEL TEMA 5 — DEMO COMPLETADA ===")
