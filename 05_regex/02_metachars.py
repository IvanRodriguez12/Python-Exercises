# El punto (.)

import re
text = "Me gusta Python me encanta Pyth0n como me gustaria ser bueno programando en Pytho00n"
pattern = r"Pyth.n" #(la r sirve para decir que estamos creando una expresion regular")

find = re.findall(pattern, text)
print(find)

text = "Mi casa es de color azul. Y el auto es rojo."
pattern = r"\."

find = re.findall(pattern, text)
print(find)

# \d sirve para encontrar cualquier dígito del 0 al 9
text = "Mi número de teléfono es 1234567890"
pattern = r"\d{9}"

found = re.findall(pattern, text)
print(found)

text = "Mi número de teléfono es +53 1234567890"
pattern = r"\+54 \d{9}"
found = re.search(pattern, text)

if found :
    print(f"Se encontro al numero {found.group()}")

# \w sirve para encontrar cualquier caracter alfanumerico
text = "@el_rubius_09"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s sirve para encontrar cualquier salto en balnco (espacio, tabulacion, etc)
text = "Hola mundo\nAy si Ay si"
pattern = r"\s"
found = re.findall(pattern, text)
print(found)

# ^ sirve para indicar el inicio de una cadena
text = "Hola mundo"
pattern = r"^\w"
valid = re.search(pattern, text)

if valid:
    print("El nombre del usuario es valido")
else:
    print("El nombre del usuario no es valido")

phone = "+54 3624393912"
pattern = r"^\+\d{2,3} "

valid = re.search(pattern, phone)

if valid:
    print("El numero ingresado es valido")
else:
    print("No")