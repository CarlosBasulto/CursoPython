# Tema 6: Expresiones regulares, errores y compresión de listas

Este tema cubre tres apartados clave: uso de **expresiones regulares** (`re`), manejo de **errores y excepciones** (`try-except`) y la **compresión de listas/diccionarios/conjuntos** para escribir código más compacto y eficiente.

**Ejemplo:**
```python
import re
texto = "Mi teléfono es 123-456"
print(re.findall(r'\d+', texto))

# Compresión de listas
nums = [i**2 for i in range(5)]
print(nums)
```

> **Nota:** Apoyo visual y ejercicios se ven en clase.
