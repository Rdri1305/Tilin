'''
Programa que usa las clases declaradas en el archivo clases.py
Fecha: 02/09/24
'''
import Clases as cl
# Crear objetos de clase persona
per1 = cl.Persona("Juan", 70)
per2 = cl.Persona("Maria", 50)
#Asignar valor a las propiedades
per1.peso = 75
per2.peso = 57
per2.nombre += " Elena"
#Usar los metodos
per1.caminar()
per2.comer()
per2.comer()
print(per1)
print(per2)
#print("Nombre y Peso: ", per1.nombre, per1.peso)
#print("Nombre {} y Peso: {} ".format(per2.nombre, per2.peso))
per1.caminar(16)
#print("Nombre {} y Peso: {} ".format(per1.nombre, per1.peso))
print(per1)
per3 = cl.Persona() #Con la sobrecarga al constructor
#print("Nombre y Peso: ", per3.nombre, per3.peso)
print(per1)
print(per2)
print(per3)

#Crear Atletas
atl1 = cl.Atleta("José", 70)
atl2 = cl.Atleta("Rosa", 50)
print('\n',atl1)
print(atl2)
#Asignar valores a la propiedad estatura
atl1.estatura = 1.65
atl2.estatura = 1.60
print(atl1)
print(atl2)
print('Atleta: {}, IMC: {: .2f}'.format(atl1.nombre, atl1.calcular_imc()))
print('Atleta: {}, IMC: {: .2f}'.format(atl2.nombre, atl2.calcular_imc()))