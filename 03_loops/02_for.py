# Ejemplo de un bucle for en Python
frutas = ["Manzana", "Banana", "Cereza", "Durazno"]

for fruta in frutas:
    print(fruta)


# Otro ejemplo con una cadena de texto pero por interación de caracteres
londrea = "Londres"

for letra in londrea:
    print(letra)


# Ejemplo de recuperar el indice enumerated()
cosas = ["Libro", "Gas", "Cartuchera"]

for index, cosa in enumerate(cosas):
    print(f"El indice de {cosa} es {index}")


# For anidados
print("\nEjemplo de For anidado: ")
letras = ["A", "B", "C"]
numeros = [1,2,3,4,5]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# RECOMENDACION PYTHON TUTOR (Te muestra que hace cada linea de tu codigo)
print("\nBreak: ")
animales = ["Perro", "Canario", "Gato", "Elefante"]

for animal in animales:
    if animal == "Gato":
        print("Se encontro al Gato")
        break
    print(animal)

print("\nContinue: ")

for animal in animales:
    if animal == "Canario":
        continue
    print(animal)

# Comprension de listas (Listas comprehesion)
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
for num_pares in range(2,22,2):
    print(num_pares)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10,20,30,40,50]
suma = 0

for numero in numeros:
    suma += numero

total = suma / len(numeros)
print(total)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros1 = [15,5,25,10,20]
mayor = 0

for numero in numeros1:
    if numero > mayor:
        mayor = numero

print(mayor)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]

palabras_largas = [palabra for palabra in palabras if len(palabra) >= 5]
print(palabras_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras1 = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = str(input("Ingrese una letra: "))

pal_con_inicial = 0

for palabra in palabras1:
    for c in palabra:
        if c == letra.lower():
            pal_con_inicial += 1
            break

print(pal_con_inicial)