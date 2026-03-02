# Son metodos porque se usan con el punto, y son funciones porque hacen algo, no solo devuelven un valor como len().

lista = [1,2,3,4,5]

lista.append(10) # inserta al final
lista.insert(1, 20) # inserta donde le digamos
lista.extend([30,10]) # agrega los elementos de la lista que le pasamos, no la lista como un elemento, como append
lista.remove(10) # borra la primera aparición de un elemento x
lista.pop() # se le puede pasar cualquier indice pero por defecto elimina el ultimo

print(lista)

# Borrar por rangos
lista2 = [32,412,423,29,3,2,4,21]
del lista2[1:3]
print(lista2)

lista.clear()


# Ordenar listas
lista3 = [2,3,4,5,6,72,123,432,543,65,129]
lista3.sort() # ordena la lista original 
print(lista3)

lista4 = [2,3,4,5,6,72,123,432,543,65,129]
lista_ordenada = sorted(lista4) # devuelve una nueva lista ordenada, no modifica la original
print(lista4)
print(lista_ordenada)

# Ordena las palabras y como estan todas en mayusculas no hay problema
lista_palabras = ["Manzana", "Pera", "Sandia"]
lista_p_ord = sorted(lista_palabras)
print(lista_p_ord)

# Ordena la lista pero siempre va a ir primera la palabra que contenga una mayúsculas y despes als demás en orden
lista_palabras2 = ["manzana", "Pera", "sandia"]
lista_p_ord2 = sorted(lista_palabras2)
print(lista_p_ord2)

# Ordena la lista normal convirtiendo las palabras en minusculas
lista_palabras2.sort(key=str.lower)
print(lista_palabras2)

# Más metodos de listas
animales = ["Panda","Panda", "Koala", "Elefante"]
print(len(animales))

print(animales.count("Panda"))

print("Koala" in animales)
print("Tortuga" in animales)

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista_ex = [1,2,3,4,5]
lista_ex.append(6)
lista_ex.insert(1, 10)
# Se puede hacer esto para insertar cualquier numero en cualquier indice y modificar el que ya estaba en ese lugar
lista_ex[0] = 0
print(lista_ex)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

print("\nNuevos ejercicios:")
lista_a = [1,2,3]
lista_b = [4,5,6,1,2]

lista_a.extend(lista_b)
lista_a.remove(1)
print(lista_a.pop(3))
lista_b.clear()
print(lista_a)
print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

print("\nOtros ejercicios:")
lista_c = [1,2,3,4,5,6,7,8,9,10]
del lista_c[2:5]
print(lista_c)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.


# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.