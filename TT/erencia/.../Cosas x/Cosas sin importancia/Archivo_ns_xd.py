class Persona:
    #def __init__(self,nombre,peso):
    # self.nombre =nombre
    # self.peso = peso
    def __init__(self,nombre,peso):
        if len(args)== 0:
          self.nombre = "sin nombre"
          self.peso = 0
        else:
           self.nombre = args[0]
           self.peso = args[1]

    def caminar(self):
        if len(args) > 0:
            self.peso -= args[0] / 8.0
        else:
          self.peso -= 0.5
    def comer(self):
        self.peso += 1
    def __str__(self):
       return "persona (nombre: {},peso: {})".format(self.nombre, self.peso)
    

    
    """
    Nueva clase: Atleta
    """
    class atleta(persona):
     estatura = 0.0
    def calcular_inc(self):
       return self.peso / (self.estatura * self.estatura)
    def __str__(self) #Permite una cadena con todos los datos
       return "atleta (nombre{}, peso={}, estatura={})".format(self.nombre, self.peso, self.estatura)