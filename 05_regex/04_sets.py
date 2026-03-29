import re

# [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
  print("El nombre de usuario es válido: ", match.group())
else:
  print("El nombre de usuario no es válido")


# Buscar todas las vocales de una palabra
text = "hola mundo"
pattern = r"[aeiou]"

find = re.findall(pattern, text)
print(find)

# buscar las palabras que terminen en an
text = "man fan ran ñan dian"
pattern = r"[mrd]an"

find = re.findall(pattern, text)
print(find)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana" 
pattern = r"\b[mfb]an\b"

matches = re.findall(pattern, text)
print(matches)


text = "22431"
pattern = r"[1-2]"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"