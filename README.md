# Ejercicio_Poo_con_Archivos

El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:

# Funcion 1
Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.
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


# Funcion 2
Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

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
        #Segundo ordinario y parcial
            if alumno['Ordinario2']:
                parcial2= nota(alumno['Ordinario2'])
            elif alumno['Parcial2']:
                parcial2= nota(alumno['Parcial2'])
            else:
                parcial2= 0
        #Practicas
            if alumno['OrdinarioPracticas']:
                practicas= nota(alumno['OrdinarioPracticas'])
            elif alumno['Practicas']:
                practicas= nota(alumno['Practicas']):
            else:
                practicas= 0
        
        #Establecemos la relacion del examen con el nombre adquirido y los porcentajes de cada examen, o practica, en su defecto

            alumno['Final1'] = parcial1
            alumno['Final2'] = parcial2
            alumno['FinalPracticas'] = practicas
            alumno['NotaFinal'] = parcial1*0.3 + parcial2*0.3 + practicas*0.4
            return alumno
    
        #Devolvemos la funcion definida arriba a todos los alumnos para que aparezcan sus calificaciones
        return list(map(nota_final, calificaciones))
# Funcion 3
Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

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

    #Ejecutamos el codigo de cada funcion
    print(nota_final_alumno(calificaciones('calificaciones.csv')))
    aprobados, suspensos = alumnos_aprobados_suspensos(nota_final_alumno(calificaciones('calificaciones.csv')))
    print('La lista de los alumnos aprobados es la siguiente: /n', aprobados)
    print('La lista de los alumnos suspensos es la siguiente: /n', suspensos)