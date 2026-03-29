# los cuantificadores se utilizan para indicar cuantas ocurrencias de un caracter 
# o un grupo de caracteres hay

# * Puede aparecer 0 o mas veces
import re
text = "aaa, assdsa, lll"
pattern = r"a*"

find = re.findall(pattern, text)
print(find)

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?

text = "aaaaaaab, ssdsadsaaa, dsadab"
pattern = r"a*b"

find = re.findall(pattern, text)
print(find)

# + una a m+as veces: 
text = "aaaaaaab, ssdsadsaaa, dsadab"
pattern = r"a+"

find = re.findall(pattern, text)
print(find)

# ? cero o una vez devuelve:
pattern = r"a?b"
text = "aaabacb"

find = re.findall(pattern, text)
print(find)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = r"\+?34|00 \d{9}"

find = re.findall(pattern, phone)
print(find)

# {n} encuentra una letra n veces
text = "ula ula uuu uu uuuu"
pattern = r"u{3}"

matches = re.findall(pattern, text)
print(matches)

# de {n} a {m} veces encuentra una letra
text = "ula ula uuu uu uuuu"
pattern = r"\w{3,4}"

matches = re.findall(pattern, text)
print(matches)

# entre
palabras = "ala casa arbol gigante rio"
pattern = r"\b\w{3,4}\b"

matches = re.findall(pattern, palabras)
print(matches)

# mas
palabras = "ala casa arbol gigante rio"
pattern = r"\b\w{5,}\b"

matches = re.findall(pattern, palabras)
print(matches)