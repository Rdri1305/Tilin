'''
Clases empleado, nombrado y parcial
Fecha: 12/09/2024
'''
class Empleado:
    def __init__(self, nombre"sin nombre"):
        self.nombre = nombre
    def calcular(self):
        pass

class Nombrado(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init(nombre) #asignar valores a la clase superior
        self.sueldo = sueldo
    def calular(self, sueldo = None):
        if sueldo is None:
            return self.sueldo
        else:
            self.sueldo = sueldo
        return self.sueldo
    
class Parcial(Empleado):
    def __init__(self, nombre, horas_trabajadas=None, tarifa_hora=None):
        super().__init__(nombre)
        if horas_trabajadas is not None:
            self.horas_trabajadas = horas_trabajadas
        if tarifa_hora is not None:
            self.tarifa_hora = tarifa_hora  
    def calcular(self, horas_trabajadas=None, tarifa_hora=None):
      
    