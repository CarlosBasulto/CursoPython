# ============================================================
# PRÁCTICA TEMA 5: MÓDULOS, PAQUETES Y POO — SOLO ENUNCIADOS
# ============================================================
# Instrucciones:
# - Este archivo contiene 10 ejercicios. Cada uno está descrito SOLO como comentarios.
# - Escribe tu solución debajo del enunciado correspondiente.
# - No borres los enunciados. Añade tu código debajo de cada bloque.
# - Puedes crear carpetas y archivos adicionales (módulos/paquetes) si el ejercicio lo pide.
# - Usa print() para mostrar resultados y comprobar que funciona.
# ============================================================

print("=== PRÁCTICA TEMA 5 — EMPIEZA AQUÍ ===\n")

# ------------------------------------------------------------
# EJERCICIO 1: Crear un MÓDULO sencillo
# Enunciado:
# 1) Crea un archivo llamado "circunferencia.py" en la misma carpeta.
# 2) Dentro define dos funciones:
#    - perimetro(r): devuelve 2 * pi * r
#    - area(r):      devuelve pi * r**2
#    (importa math para usar math.pi)
# 3) En este script principal, importa el módulo y:
#    - Calcula perímetro y área para r=5 y muéstralos.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 2: Import con ALIAS y FROM ... IMPORT
# Enunciado:
# 1) Importa el módulo "circunferencia" con alias "circ".
# 2) Importa SOLO la función area con: from circunferencia import area
# 3) Llama a circ.perimetro(10) y a area(10) y muestra resultados.
# 4) Explica en un comentario cuándo preferirías alias vs from-import.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 3: Crear un PAQUETE "figuras"
# Enunciado:
# 1) Crea una carpeta "figuras/" con:
#    - __init__.py  (puede comenzar vacío)
#    - circunferencia.py  (puedes reutilizar el del Ej.1)
#    - poligono.py (crea funciones: perimetro_regular(lado, n), area_regular(lado, n))
# 2) En __init__.py exporta todo lo necesario (from .circunferencia import ...).
# 3) En este script: importa el paquete "figuras" y usa sus funciones.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 4: FROM paquete IMPORT módulo(s)
# Enunciado:
# 1) Importa desde el paquete "figuras" SOLO el módulo "poligono".
#    (pista: from figuras import poligono)
# 2) Llama a poligono.area_regular(lado=6, n=5) y muéstralo.
# 3) Importa con alias (as pol) y vuelve a llamar a sus funciones.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 5: DOCSTRINGS de módulo y help()
# Enunciado:
# 1) Añade un docstring al inicio de circunferencia.py explicando qué hace el módulo
#    y listando brevemente sus funciones.
# 2) Desde este script, importa circunferencia y muestra:
#    - print(circunferencia.__doc__)
#    - help(circunferencia)
# 3) Comenta brevemente (en comentarios) por qué documentar módulos es útil.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 6: Clase LIBRO (POO básica)
# Enunciado:
# 1) Define una clase Libro con atributos: titulo, autor, isbn, paginas (int), edicion (int).
# 2) Implementa __init__ para inicializar (titulo, autor, isbn) y valores por defecto para el resto.
# 3) Implementa un método descripcion() que devuelva "TÍTULO - AUTOR (ISBN ...)".
# 4) Crea dos instancias y muestra sus descripciones.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 7: Métodos y __str__
# Enunciado:
# 1) En la clase Libro añade:
#    - un método actualizar_edicion(nueva_edicion:int)
#    - __str__ para mostrar un texto legible del objeto
# 2) Crea un libro, actualiza su edición y haz print(libro) para ver __str__.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 8: HERENCIA — Persona, Alumno, Profesor
# Enunciado:
# 1) Crea una clase base Persona con atributos: nombre, nacimiento (str o date), domicilio.
#    - método cambiar_domicilio(nuevo)
#    - __str__ que resuma los datos
# 2) Crea Alumno(Persona):
#    - atributos adicionales: asignatura, calificacion (None por defecto)
#    - método poner_calificacion(nota)
# 3) Crea Profesor(Persona):
#    - atributos adicionales: especialidad, asignaturas_impartidas (lista)
#    - método agregar_asignatura(nombre)
# 4) Crea 1 Alumno y 1 Profesor, muestra __str__, usa sus métodos y verifica que heredan correctamente.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 9: SOBRECARGA/ESPECIALIZACIÓN de método
# Enunciado:
# 1) En Profesor, sobreescribe __str__ para incluir la especialidad y el número de asignaturas impartidas.
# 2) En Alumno, sobreescribe __str__ para incluir la asignatura y la calificación (o "Sin calificar").
# 3) Muestra por pantalla ambos __str__ y comenta (en comentarios) el concepto de polimorfismo.
# ------------------------------------------------------------



# ------------------------------------------------------------
# EJERCICIO 10: COMPOSICIÓN y MÓDULOS combinados
# Enunciado:
# 1) Crea un módulo "biblioteca.py" con una clase Biblioteca que:
#    - tenga un atributo "catalogo" (lista de Libro)
#    - métodos: agregar_libro(libro), buscar_por_titulo(titulo)->Libro|None, listar()
# 2) Importa Biblioteca aquí, crea 3 libros y añádelos al catálogo.
# 3) Busca por título uno de ellos y muéstralo.
# 4) Llama a listar() para mostrar todo el catálogo.
# 5) Explica (en comentarios) la diferencia entre herencia y composición.
# ------------------------------------------------------------



print("\n=== FIN DE LA PRÁCTICA TEMA 5 — ¡BUEN TRABAJO! ===")
