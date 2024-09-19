'''
Clases a usar en nuesros proyectos
Fecha: 02/09/24
'''
class Persona:
    #def _init_(self,nombre, peso):
     #   self.nombre = nombre
      #  self.peso = peso
    def _init_(self, *args):
        if len(args) == 0:
            self.nombre = 'Sin nombre'
            self.peso = 0
        else:
            self.nombre = args[0]
            self.peso = args[1]
            #Lo de arriba es un constructor con argumentos
    def caminar (self, *args):
        if len(args) > 0:
            self.peso -= args[0] / 8.0
        else:
            self.peso -= 0.5
    def comer (self):
        self.peso += 1
    def _str_(self):
        return 'Persona (nombre: {}, peso: {})'.format(self.nombre, self.peso
        )
    
""""
Nueva Clase: Atleta
"""
class Atleta (Persona):
    estatura = 0.0
    def calcular_imc (self):
        return self.peso / (self.estatura * self.estatura)
    def _str_(self): #Permite obtener una cadena con todos los valores
        return 'Atleta (nombre: {}, peso: {}, estatura: {}'.format(self.nombre, self.peso, self.estatura
        )