##
# 01 - Expresiones regulares
# 

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

import re

pattern = "Hola"
text = "Hola mundo"

result = re.search(pattern, text)

if result:
    print("Encontramos el patron")
else:
    print("No encontramos el patron jeje")

# group() devuelve la cadena que coincide con el pattern
print(result.group())

# start() donde empieza
print(result.start())

# end() donde termina
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
encontrar_patron = re.search(pattern, text, re.IGNORECASE)

if encontrar_patron:
    print(f"Encontramos el patron en {encontrar_patron.start()} y terminaba en {encontrar_patron.end()}")

# Encontrar todas las ocurrencias de un patron

text = "Me gusta Python me encanta Python como me gustaria ser bueno programando en Python"

# se puede poner un punto en el lugar de una letra para que te encuentre una ocurrencia con cualquier letra en esa parte
pattern = "Pytho."

matches = re.findall(pattern, text)
print(matches)

# .iter() devuelve un iterador con las coincidencias encontradas
matches_iter = re.finditer(pattern, text)
for match in matches_iter:
    print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

### Modificadores

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

pattern = "midu"

matches = re.findall(pattern, text)

matches_iter = re.finditer(pattern, text)
for match in matches_iter:
    print(match.group(), match.start(), match.end())

#regular expressions 111

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"

pattern = "Python"

encontrar_patron = re.findall(pattern, text, re.IGNORECASE)
print(encontrar_patron)
print(len(encontrar_patron))


# .sub() reemplaza todas las coincidencias de un patrón en un texto
text = "Hola mundo jaja si, hola a todos"
pattern = "Hola"
replacement = "Adios"

reemplazar_patron = re.sub(pattern, replacement, text,count=0)
print(reemplazar_patron)
