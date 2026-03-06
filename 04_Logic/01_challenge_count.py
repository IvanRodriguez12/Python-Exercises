"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. 
En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece 
la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en 
equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), 
por lo que la función debe retornar True.
"""

# Como lo resolvi
def en_equilibrio(frase):
    frase = frase.lower()
    mr_fantastic = 0
    antorcha_humana = 0

    for palabra in frase:
        for c in palabra:
            if c == "r":
                mr_fantastic += 1
            elif c == "j":
                antorcha_humana += 1
    
    if mr_fantastic > antorcha_humana:
        print(False) 
    elif antorcha_humana > mr_fantastic:
        print(False)
    else:
        print(True)

en_equilibrio("hola si R")

# Mejora
def en_equilibrio1(frase):
    frase = frase.lower()
    conR = frase.count("r") 
    conJ = frase.count("j")

    print(f"conR: {conR}, conJ: {conJ}")

    return conR == conJ

print(en_equilibrio1("hola si R"))
print(en_equilibrio1("hola si Rj"))
print(en_equilibrio1("hola si j"))

