#Creando lista con list()
lista = list([23, False, True])

#Cantidad de elmentos en una lista
cantidad_elementos = len(lista)

#Agregando elemento a un alista
lista.append(78)

#Agregar elemento a una lista desde indice
lista.insert(0,6)

#agregar varios elementos a la lista
lista.extend([1])

#Eliminando elemento de la lista desde el indice
lista.pop(-1)

#Removiendo un elemento de la lista por su valor
lista.remove(6)

#Eliminar todos los elementos de la lista
#lista.clear()

#Ordenando lista
#reverse=True ordena de mayor a menor
lista.sort()

#Invirtiendo los elementos de una lista
lista.reverse()

print(lista)
