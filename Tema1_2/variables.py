# ============================================
# PRIMEROS PASOS EN PYTHON: VARIABLES Y TIPOS
# ============================================

# En Python no necesitamos declarar el tipo de la variable explícitamente,
# el intérprete lo infiere automáticamente según el valor asignado.
# A esto se le llama "tipado dinámico".

# Ejemplo de diferentes tipos de variables:
entero = 10                 # Variable de tipo int (número entero)
decimal = 3.14              # Variable de tipo float (número decimal)
texto = "Hola, mundo"       # Variable de tipo str (cadena de texto)
booleano = True             # Variable de tipo bool (booleano: True o False)

# Podemos imprimir el contenido de las variables con print()
print("Valor de entero:", entero)
print("Valor de decimal:", decimal)
print("Valor de texto:", texto)
print("Valor de booleano:", booleano)

# Con type() podemos comprobar el tipo de dato de cada variable
print("Tipo de 'entero':", type(entero))
print("Tipo de 'decimal':", type(decimal))
print("Tipo de 'texto':", type(texto))
print("Tipo de 'booleano':", type(booleano))

# ============================================
# CAMBIO DE VALORES Y TIPOS
# ============================================

# Las variables en Python pueden cambiar de valor y de tipo en cualquier momento
x = 5            # x empieza siendo un número entero
print("x vale:", x, "y es de tipo", type(x))

x = "ahora soy texto"  # x ahora es una cadena de texto
print("x vale:", x, "y es de tipo", type(x))

# ============================================
# OPERACIONES BÁSICAS
# ============================================

a = 7
b = 2

# Suma, resta, multiplicación, división
print("Suma:", a + b)             # 7 + 2 = 9
print("Resta:", a - b)            # 7 - 2 = 5
print("Multiplicación:", a * b)   # 7 * 2 = 14
print("División:", a / b)         # 7 / 2 = 3.5

# División entera (descarta decimales) y resto
print("División entera:", a // b) # 7 // 2 = 3
print("Resto:", a % b)            # 7 % 2 = 1

# Potencias
print("Potencia:", a ** b)        # 7^2 = 49

# ============================================
# ENTRADA DE DATOS
# ============================================

# La función input() permite pedir datos al usuario (se leen como texto)
nombre = input("Escribe tu nombre: ")
print("Hola,", nombre)

# Para convertir el texto a número debemos usar int() o float()
edad = int(input("¿Cuántos años tienes?: "))
print("Dentro de 5 años tendrás:", edad + 5)

# ============================================
# RESUMEN
# ============================================
# 1. Python usa tipado dinámico (no declaramos tipo).
# 2. type() sirve para comprobar el tipo de una variable.
# 3. Una variable puede cambiar de tipo en cualquier momento.
# 4. input() recoge datos como texto, pero podemos convertirlos.
