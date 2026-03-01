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
lista3.sort()
print(lista3)