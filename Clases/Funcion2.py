#Enunciado
#Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

#Importamos la funcion 1
from Funcion1 import Funcion1

#Definimos la lista de diccionarios con las calificaciones de cada alumno al calcular la nota final.
def nota_final_alumno(calificaciones):
    def nota_final(alumno):
        #Establecemos las relaciones que existen dependiendo del examen al que se presente y la nota obtenida en este.
        #Primera ordinario y parcial
        if alumno['Ordinario 1']: 
            parcial1= nota(alumno['Ordinario1'])
        elif alumno['Parcial1']:
            parcial1= nota(alumno['Parcial1'])
        else:
            parcial1= 0
       