import clases_y_objetosas cl
# Crear objetos de clase Persona
per1 = cl.persona("juan", 70)
per2 = cl.persona("María", 55)
# Asignar valor a las propiedades
per1.peso = 75
per2.peso = 57
per2.nombre += " Elena"
#Usar los metodos
per1.caminar()
per2.comer()
per2.comer()
print("Nombre: {} Peso: {}",format(per1. nombre, per1.peso))
print("Nombre: {} Peso: {}",format(per2. nombre, per2.peso))
per1.caminar(16)
print("Nombre: {} y peso: {}".format(per1.nombre, per1.peso))
per1.caminar()
print("Nombre: {} y peso: {}".format(per1.nombre, per1.peso))
per3= cl.Persona() # con la sobrecarga al constructor
print("Nombre: {} y peso: {}".format(per3.nombre, per3.peso))

#Crear atletas
atl1 = cl.Atleta("José", 70)
atl2 = cl.Atleta("Rosa", 50)
print(atl1)
print(atl2)
#Asignar valores a la propiedad estatura
atl1.estatura = 1.65
atl2.estatura =1.60
print(atl1)
print(atl2)
print("atleta: { }, Imc={}". firnat(atl1.nombre, atl1.calcular_inc()))
print("atleta: { }, Imc={}". firnat(atl2.nombre, atl2.calcular_inc()))