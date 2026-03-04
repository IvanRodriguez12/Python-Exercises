# bucles while

contador = 0

#while contador <= 5:
#    print(contador)
#    contador += 1

# Bucle while infinito se corta con break cuando cumple una condicion
while True:
    print(contador)
    contador+=1
    if contador == 5:
        break

# Bucle while con continue para saltar una iteracion
print("\nBucle con continue: ")
cont = 0

while cont < 10:
    cont += 1

    if cont % 2 == 0:
        continue

    print(cont)

# Bucle con Else sirve por ejemplo para saber exactamente que el bucle reviso todo y terminó (no break)
print("\nBucle con else: ")
contador1 = 0

while contador1 < 10:
    print(contador1)
    contador1 += 1
else:
    print("El bucle ha terminado")

# Pedir datos al usuario
numero = -1

#while numero <= 0:
#    try: 
#        numero = int(input("\nIngresa un numero positivo: "))
#        if numero <= 0:
#            print ("Ingresa un numero positivo putamae")
#    except:
#        print("Eso no es un numero, ingresa un numero positivo")
#print("Bien ahi pa es positivo ")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

print("\nEjercicio 1:")
num = 10

while num >= 1:
    print(num)
    num = num - 1


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

print("\nEjercicio 2:")
num1 = 0
suma = 0

while num1 <= 20:
    if num1 % 2 == 0:
        suma = num1 + suma
    num1 += 1
print(f"\nLa suma de los numeros pares del 1 al 20 es de: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

print("\nEjercicio 3:")
num2 = 0
num3 = 1
factorial = 1


while num2 <= 0:
    try:
        num2 = int(input("Ingrese un numero: "))
        if num2 <= 0:
            print("Ingresa un numero positivo mamonson")
        else:
            while num3 <= num2:
                factorial = factorial * num3
                num3 += 1
        print(f"\nEl factorial de {num2} es {factorial}")
    except:
        print("Ingresa un numero positivo no otra cosa")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")