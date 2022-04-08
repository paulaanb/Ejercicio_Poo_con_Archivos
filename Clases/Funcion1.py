# Enunciado
#Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

#Empezamos definiendo la nota

def nota(numero):
    numero = numero.replace(',', '.') #Con esto lo que hacemos es cambiar la coma que separa el numero entero de los decimales por un punto.
    return float(numero)

#Definimos la calificacion de las notas

def calificaciones(sumatoria):
    #Vamos  a crear una funcion para que devuelva los datos del archivo csv en forma de lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno.
    #Abrimos el archivo para leerlo
    try:
        f= open(sumatoria, 'r')
    #Establecemos la excepcion
    except FileNotFoundError:
        print("El fichero seleccionado no existe.")
        return
    #Ahora leemos el archivo en forma de lista(que ya definimos antes) y lo cerramos.
    leerlista = f.readleerlista()
    f.close()
    
    #Establecemos unos comandos para que al imprimir la lista aparezca de forma ordenada.
    comando= leerlista[0][:-1].split(";")
    calificaciones=[]

    #Añadimos el diccionario creado a la lista de calificaciones
    for i in leerlista[1:]:
        valor = i[:-1].split(";")
        alumno ={}
        for j in range(len(valor)):
            alumno[comando[j]] = valor[j]
            calificaciones.append(alumno)
    return calificaciones

#Ya hemos realizado la lista de calificaciones ordenadas por apellido
