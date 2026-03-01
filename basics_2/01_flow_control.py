edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

print("\n")
licencia = input("Tienes licencia de conducir? (si/no): ").lower()

if edad >= 18 and licencia == "si":
    print("Puedes conducir")