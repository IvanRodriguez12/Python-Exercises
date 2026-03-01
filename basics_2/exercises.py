from os import system
if system("clear") != 0: system("cls")

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
#
num1 = input("Introduce un numero: ")
num2 = input("Introduce otro numero: ")

if num1 < num2:
    print(f"El numero {num2} es mayor")
elif num2 < num1:
    print(f"El numero {num1} es mayor")
else:
    print("Son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num3 = int(input("Introduce un numero: "))
num4 = int(input("Introduce otro numero: "))
signo = input("Introduce un signo: ")

if signo == "-": 
   print(num3 - num4)
elif signo == "+":
    print(num3 + num4)
elif signo == "*":
    print(num3 * num4)
elif signo == "/":
    if num3 == 0 or num4 == 0:
       print("No se permite dividir por 0")
    else:
        print(num3 / num4)


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} No es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Ingrese su edad: "))

if edad >= 65:
    print("Usted es un Adulto mayor")
elif edad >= 18:
    print("Usted es un adulto")
elif edad >= 13:
    print("Usted es un adolescente")
elif edad >= 3:
    print("Usted es un niño")
else:
    print("Usted es un bebé")