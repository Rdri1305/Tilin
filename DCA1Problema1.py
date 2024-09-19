class Persona:
    def __init__(self, nombre, distancia_recorrida=0):
        self.Nuñez_nombre = nombre
        self.Nuñez_distancia_recorrida = distancia_recorrida #En kilometros
        
        def caminar(self):
            return distancia_recorrida + 2
        
       
class Atleta(Persona):
        def __init__(self, nombre, distancia_recorrida = 0, calorias_consumidas = 0):
            super().__init__(nombre, distancia_recorrida)
            self.Nuñez_calorias_consumidas = calorias_consumidas
            
            
        def entrenar(self, distancia = 10): #Cuando se entrene se llama a este
            self.Nuñez_distancia_recorrida += distancia
            self.Nuñez_calorias_consumidas = distancia * 500 #Las cal consumidas se multiplican x la distancia recorrida
             
        def competir(self, distancia = 20): #Si se compite se llama a este
            self.Nuñez_distancia_recorrida += distancia
            self.Nuñez_calorias_consumidas = distancia * 750 #Las cal consumidas se multiplican x la distancia recorrida
            #Haci no defines mas objetos y dependiendo de lo que haga la persona el codigo lo realiza
            
            
            
            
#Unittest :3
import unittest

class testPersona(unittest.TestCase):
    def test_Persona(self):
        Nuñez_per1 = Persona('Joaquin')
        Nuñez_per1.caminar()
        self.assertEqual(Nuñez_per1.Nuñez_distancia_recorrida, 100)
        
    def test_entrenar(self):
        Nuñez_per2 = Persona('Tilino')
        Nuñez_per2.entrenar()
        self.assertEqual(Nuñez_per2.Nuñez_distancia_recorrida, 100)
        
    def test_competir(self):
        Nuñez_per3 = Persona('Joaquin')
        Nuñez_per3.competir()
        self.assertEqual(Nuñez_per3.Nuñez_distancia_recorrida, 100)
        
if __name__ == '__main__':
 unittest.main()