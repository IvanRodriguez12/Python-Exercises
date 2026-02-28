print(type("mamameelmounstruo"))  # str
print(type(5)) # int
print(type(3.14)) # float
print(type(True)) # bool
print(type(1+2j)) # complex
print(type(None)) # NoneType


iva = 0.21
print(type(iva))

print("\n")
numero = int(input("Ingrese un numero: "))

calculadora_iva = numero * iva 
precio_final = numero + calculadora_iva

print(calculadora_iva)

print(f"El precio final es de: {precio_final}")