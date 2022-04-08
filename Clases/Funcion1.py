# Enunciado
#Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

#Empezamos definiendo la nota

def nota(numero):
    numero = numero.replace(',', '.') #Con esto lo que hacemos es cambiar la coma que separa el numero entero de los decimales por un punto.