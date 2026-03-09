# Diccionarios, son colecciones de clave-valor y sirven para guardar datos relacionados
persona = {
    "nombre": "Juan",
    "edad": 20,
    "sexo": "hombre",
    "running_in_the_90s": True,
    "calificaciones": [5,8,9],
    "redes_sociales": {
        "whatsapp": True
    }
}

# Acceder a uno de los campos
print(persona["nombre"])
print(persona["redes_sociales"]["whatsapp"])
print(persona["sexo"])

# Eliminar una clave-valor
del persona["edad"]
print(persona)

# Cambiar un valor
persona["Sexo"] = "Mujer"
persona["calificaciones"][1] = 2 

# Eliminar un campo y devolverlo
is_running = persona.pop("running_in_the_90s")
print(is_running)
print(persona)


# Sobreescribir los valores de un diccionario
a = {"nombre": "juan Carlos", "edad": 20, "tiene_licencia": True, "embarazada": False}
b = {"nombre": "juan ", "edad": 20, "tiene_licencia": False, "Tiene_hijos": True}


print("\n")
print(a)
print(b)

a.update(b)
print(a)

# Verificar que un diccionario tenga ese campo
print("nombre" in persona)
print("religion" in persona)

# Traer los valorres o las claves
print(persona.values())
print(persona.keys())

for key, value in persona.items():
    print(f"{key}: {value}")