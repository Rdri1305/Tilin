import unittest
from Clases_empleado import Empleado, Gerente

class testEmpleado(unittest.TestCase):
    def test_propiedades_empleado(self):
        emp1 = Empleado('Juan', 20, 2000)
        self.assertEqual(emp1, __str__(),'Empleado => nombre: Juan')
        
    def test_bono_empleado(self):
        emp = Empleado ('Maria', 25, 2000)
        self.assertEqual(emp.calcular_bono(), 200)
        
    def test_propiedades_gerente(self):
        pass
    
    def test_bono_gerente(self):
        per1
    
     
     
     
     
     
     
     
     
'''
Herencia de producto y perecible
'''
from datetime import datetime

class Producto:
    def __init__(self, precio=None, stock=None):
        self.precio = 0.0
        self.stock = 0
        if precio:
            self.precio = precio
        if stock:
            self.stock = stock
    def inventario_valorizado(self):
        return  self.precio * self.stock

    def __str__(self):
        return f'producto (precio: {self.precio}, stock: {self.stock})'


class Perecible(Producto):
    def __init__(self, precio=None, stock=None, fecha_vencimiento='2025-09-16'):
        super().__init__(precio, stock)
        self.fecha_vencimiento = datetime.now().date()
        if fecha_vencimiento:
            self.fecha_vencimiento = datetime.strptime(fecha_vencimiento,"%Y-%m-%d").date()
        
    def sacar(self, cantidad):
        self.stock -= cantidad

    def poner(self, cantidad):
        self.stock += cantidad

    def inventario_valorizado(self):
        if self.fecha_vencimiento <  datetime.now().date():
            return 0.5 * super().inventario_valorizado()
        return super().inventario_valorizado()
    
    def __str__(self):
        return f'Perecible (precio: {self.precio}, stock: {self.stock}, fecha_vencimiento: {self.fecha_vencimiento})'
    
    
    
     
     
     
import unittest

class TestPrograma(unittest.TestCase):
    # Métodos de Prueba
    def test_producto_sin_argumentos(self):
        prd1 = Producto()
        self.assertEqual(prd1.inventario_valorizado(), 0)

    def test_perecible_vigente(self):
       per1 = Perecible(5, 150, '2024-12-01')
       self.assertEqual(per1.inventario_valorizado(), (5*150))

    def test_perecible_vencido(self):
       per1 = Perecible(5, 150, '2024-09-01')
       self.assertEqual(per1.inventario_valorizado(), (5*150/2))

if __name__ == '__main__':
 unittest.main()
