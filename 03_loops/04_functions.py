# Parametros es lo que pide la funcion, argumentos es lo que se le da a la funcion
def saludar():
    print("Hola")
saludar()

# Argumentos por posición, depende siempre de cual esta primero, segundo, etc
def sumar(a, b):
    """Se pasan dos numeros y se suman"""
    return a + b

resultado = sumar(14,12)
print(resultado)

# Argumentos por clave
# Parámetros nombrados

def describir_persona(nombre, edad, sexo):
    print(f"Hola {nombre}, tienes {edad} anos y eres {sexo}")

describir_persona(nombre="Juan", sexo="Lagarto", edad=18)


# Funciones con *args y **kwargs

# *args se utiliza cuando no se sabe exactamente cuantos parametros va a pasar el usuario
def multiplicar(*args):
    multiplicacion = 1
    for numero in args:
        multiplicacion *= numero 
    return multiplicacion

m1 = multiplicar(1,2,3,4,5,6,7)
m2 = multiplicar(1,2,4)
m3 = multiplicar(2,3)

print(m1)
print(m2)
print(m3)

# **kwargs se usa para pasar los argumentos en pares de clave-valor ITEMS SI QUIERO VER UNO POR UNO 

def membresia(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print("\n")
membresia(nombre="Juan Cho", Pago_membresia=True)
print("\n")
membresia(nombre="Maria", Pago_membresia=True, debe_dos_meses=False)
print("\n")
membresia(nombre_apellido="Agarra Meltro", Pago_membresia=True, es_calvo=True)
print("\n")
membresia(nombre="Julian", Pago_membresia=False) 