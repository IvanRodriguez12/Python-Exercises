"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""
# Para ver si un número es par
# siempre usamos el módulo %
# nos da el resto de la división: eggs % 2 == 2

def Huevos_carnivoros(lista_huevos) -> int:
    suma_huevos = 0
    for h in lista_huevos:
        if h % 2 == 0:
            suma_huevos += h
    return(suma_huevos)

lista_huevos = [1,2,3,4,5,6,7,8,9]
resultado = Huevos_carnivoros(lista_huevos)
print(resultado)