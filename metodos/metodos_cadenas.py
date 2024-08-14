cadena1 = "Hola,Bryan,que,hace"
cadena2 = "Bienvenido"

#Convierte a mayusculas
minus = cadena1.upper()

#Convierte a minusculas
mayus = cadena1.lower()

#Primer letra en mayuscula
primer_letra_mayus = cadena1.capitalize()

#Buscar cadena en otra cadena 
#-1 si no hay coincidencias
busqueda_find = cadena1.find("Bryan")

#Buscamos una cadena en otra cadena
#Error (Excepcion) si no hay coincidencias
busqueda_index = cadena1.index("Bryan")

#Si es numerico TRUE, si no False
es_numerico = cadena1.isnumeric()

#Si es Alfanumerico TRUE, si no TFALSE 
es_alfanumerico = cadena1.isalpha()

#Buscamos una cadena en otra cadena y devuelve la cantidad de veces que se repite
contar_coincidencias = cadena1.count("a")

#Contamos la cantidad de caracteres de una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si si devuelve TRUE
empieza_con = cadena1.startswith("H")

#Verificamos si una cadena termina con otra cadena dada, si si devuelve TRUE
termina_con = cadena1.endswith("n")

#Reemplaza un pedazo de la cadena por otra 
cadena_nueva = cadena1.replace("Hola", "Welcome")
cadena_nueva_2 = cadena_nueva.capitalize()

#separa cadenas con la cadena que le demos
cadena_separada = cadena1.split(",")

print(cadena1, cadena_separada)