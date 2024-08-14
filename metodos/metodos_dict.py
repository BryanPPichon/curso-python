diccionario = {
    "nombre": 'Bryan',
    "apellido": 'Pichon',
    "edad": 23
}

#Nos devuelve un objeto de tipo dic_items
claves = diccionario.keys()

#Obtener elemento con get(), si no encuentra nada el programa continua 
valor_de_gg = diccionario.get('gg')

#Eliminando todo del diccionario 
#diccionario.clear()

#Eliminando un elemento del diccionario
diccionario.pop("apellido")

#Obtener un elemento dic_items iterable 
diccionario_iterable = diccionario.items()

print(diccionario_iterable)