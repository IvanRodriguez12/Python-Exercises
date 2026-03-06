from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
nombre = input("Introduce tu nombre: ")
ciudad = input("Introduce tu ciudad: ")

print(f"Hola {nombre},", f"vives en {ciudad}", sep="\n")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
print(type(cadena))
entero = int(cadena)
print(type(entero))
flo = float(cadena)
print(type(flo))

print("\n")
num = 3.99
num2 = int(num)
print(f"{num}, {num2}")


print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre = "Ivan"
edad = 20
altura = 1.70

print("\n")
print(f"Hola soy {nombre}, tengo {edad} años y una altura de {altura}")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

redondeo = round(3.14)
resultado = int(redondeo / 2)

print("\n")
print(resultado)