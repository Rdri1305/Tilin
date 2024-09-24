'''
Gestión de listas, colas y pilas
'''
#Declaración de una lista
alumnos = []
#print (alumno)
alumnos.append('Juan')
alumnos.append('Rosa')
alumnos.append('Maria')
alumnos.append('Jose')
alumnos.append('Luis')
print (alumnos)

for elem in range(len(alumnos)):
    print(alumnos[elem])
    
alumnos.pop()
print(alumnos)
alumnos.pop()



from clases_lista import Listas_2
    