import unittest

# Clase Persona
class Alumno_Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.distancia_recorrida = 0

    def caminar(self):
        self.distancia_recorrida += 2  # Caminar incrementa 2 kms


# Clase Atleta, que hereda de Persona
class Alumno_Atleta(Alumno_Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.calorias_consumidas = 0

    def entrenar(self, distancia=10):
        self.distancia_recorrida += distancia
        self.calorias_consumidas += distancia * 500  # 500 calorías por km

    def competir(self, distancia=20):
        self.distancia_recorrida += distancia
        self.calorias_consumidas += distancia * 750  # 750 calorías por km

# Pruebas unitarias con unittest
class TestAlumno_Atleta(unittest.TestCase):
    def setUp(self):
        self.atleta = Alumno_Atleta("Juan")

    def test_caminar(self):
        self.atleta.caminar()
        self.assertEqual(self.atleta.distancia_recorrida, 2)

    def test_entrenar_sin_argumentos(self):
        self.atleta.entrenar()
        self.assertEqual(self.atleta.distancia_recorrida, 10)
        self.assertEqual(self.atleta.calorias_consumidas, 5000)

    def test_entrenar_con_argumentos(self):
        self.atleta.entrenar(5)
        self.assertEqual(self.atleta.distancia_recorrida, 5)
        self.assertEqual(self.atleta.calorias_consumidas, 2500)

    def test_competir_sin_argumentos(self):
        self.atleta.competir()
        self.assertEqual(self.atleta.distancia_recorrida, 20)
        self.assertEqual(self.atleta.calorias_consumidas, 15000)

    def test_competir_con_argumentos(self):
        self.atleta.competir(30)
        self.assertEqual(self.atleta.distancia_recorrida, 30)
        self.assertEqual(self.atleta.calorias_consumidas, 22500)

if __name__ == "__main__":
    unittest.main()
