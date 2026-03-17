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
