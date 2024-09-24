
import math

class Figura:
    def __init__(self, base = 0, altura = 0):
        self.base = base
        self.altura = altura
        
    def area(self):
        pass
    def perímetro(self):
        pass
    
class Rectangulo(Figura):
    
    def area(self):
        return self.base * self.altura
    
    def perímetro(self):
        return 2 * (self.base + self.altura)
    
class TrianguloRectangulo(Rectangulo):
    def area(self):
        return super().area() /2
    def perimetro(self):
        hipot = math.sqrt(math.pow(self.bsae, 2) + math.pow(self.atura, 2))
    
    
    
import unittest
class TestPrograma(unittest.TestCase):
    def test_area_rectangulo(self):
        rect = Rectangulo(4 , 3)
        self.assertEqual(rect.area(), 12)
    def test_perimetro_rectangulo(self):
        rect = Rectangulo(5, 4)
        self.assertEqual(rect.perímetro(), 18)
        
    def test_area_triangulo_rectangulo(self):
        tria = TrianguloRectangulo(3, 4)
        self.assertEqual(tria.area(), 6)
    def test_perimetro_triangulo_rectagulo(self):
        tria = TrianguloRectangulo(3, 4)
        self.assertEqual(tria.perímetro(), 12)
        
if __name__ == '__main__':
    unittest.main()

    
    
    
    
    
    
    
    
    
    
    
