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