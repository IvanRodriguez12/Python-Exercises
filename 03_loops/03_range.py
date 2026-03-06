nums = range(5) # NO ES UNA LISTA

for num in range(5):
    print(num)

print("\nRangos del 0 al 10 cada 2:")
for num in range(0,11,2):
    print(num)

print("\nRangos negativos y positivos: ")
for num in range(-5,15):
    print(num)

    
print("\nRangos negativos: ")
for num in range(0,-15,-2):
    print(num)

# Tambien se pueden hacer listas con los rangos. Por ejemplo:
numeros = range(10)
lista_de_num = list(numeros)
print(lista_de_num)

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
for numero in range(1,11):
    print(numero)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
for numero in range(1,21,2):
    print(numero)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for multilplo in range(5,51,5):
    print(multilplo)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for numero in range(10, 0, -1):
    print(numero)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = 0

for num in range(1, 101):
    suma += num

print(suma)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

numero_usuario = int(input("Ingrese un numero: "))
resultado = 0

for i in range(1,11):
    print(f"{numero_usuario} X {i} = {numero_usuario * i}")
    