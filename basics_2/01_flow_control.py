from os import system
if system("Clear") != 0: system("cls")

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

print("\n")
licencia = input("Tienes licencia de conducir? (si/no): ").lower()

if edad >= 18 and licencia == "si":
    print("Puedes conducir")

edad2 = 20
tiene_dinero = False

if edad2 >= 18:
    print ("Puedes entrar a la discoteca, eres mayor de edad")
elif tiene_dinero == True:
    print("Puedes entrar a la discoteca, tienes dinero")
else: 
    print("No puedes entrar")