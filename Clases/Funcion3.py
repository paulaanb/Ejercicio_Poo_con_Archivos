#Enunciado
#Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

from Funcion1 import Funcion1
from Funcion2 import Funcion2

#Definimos una funcion que nos indique los alumnos que estan aprobados y los que estan suspensos en forma de lista.
def alumnos_aprobados_suspensos(calificaciones):
    aprobados= []
    suspensos= []
    for alumno in calificaciones:
        if all([int(alumno['Asistencia'][:-1]) >= 75, alumno['Final1'] >= 4, alumno['FinalPracticas'] >=4, alumno['NotaFinal'] >=5):
            aprobados.append(alumno['Apellidos'] + ' , ' + alumno['Nombre'])
        else:
            suspensos.append(alumno['Apellidos'] + ' , ' + alumno['Nombre'])
        return aprobados, suspensos
    