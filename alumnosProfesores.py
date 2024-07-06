#Programa que pide el nombre y edad de un numero determinado de alumnos y determina que el mayor sera el profesor y el menor su asistente

def obtener_compañeros(cantidad): #creamos una función para obtener los datos de los alumnos y decidir quien es el profesor y quien el asistente
    compañeros = []
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del alumno: ")
        edad = int(input("ingrese la edad del alumno: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key = lambda x:x[1]) #key representa lo que debe tener en cuenta el metodo sort para ordenar los elementos de la lista
    asistente = compañeros[0][0] #El primer indice hace referencia a la tupla de datos nombre y edad y el segundo indica el nombre
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(5)
print(f"El profesor es {profesor} y su asistente es {asistente}")    