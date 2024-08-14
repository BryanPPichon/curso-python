
#Creando una lista (se puede modificar)
lista = ["Bryan","Pichon",True, 1.76]

#Creando una tupla (no se puede modificar)
tupla = ("Bryan","Pichon",True, 1.76)

#Esto es valido
lista[3] = 1.81

#esto no es valido
#tupla[3] = 1.81

#Creando un conjunto (set)
#No se pueden repetir elementos
#No se pueden acceder por indice
conjunto = {"Bryan","Pichon",True, 1.76}

#Creando un diccionario (dict)
diccionario = {
    "nombre": "Bryan",
    "apellido": "Pichon",
    "estudiante": True,
    "estatura": 1.76,
    "dato_duplicado": "Bryan"
}

print(diccionario["estatura"] + 1)