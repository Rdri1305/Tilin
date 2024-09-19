# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        raise NotImplementedError("Subclases deben implementar este método")

    def __str__(self):
        return f'{self.__class__.__name__}(nombre: {self.nombre}, edad: {self.edad})'

# Clase derivada para Perro
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def hacer_sonido(self):
        return "Guau"
    
    def __str__(self):
        return f'Perro(nombre: {self.nombre}, edad: {self.edad})'

# Clase derivada para Gato
class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def hacer_sonido(self):
        return "Miau"
    
    def __str__(self):
        return f'Gato(nombre: {self.nombre}, edad: {self.edad})'

# Ejemplo de uso
if __name__ == "__main__":
    perro = Perro("Rex", 5)
    gato = Gato("Whiskers", 3)
    
    print(perro)          # Imprime: Perro(nombre: Rex, edad: 5)
    print(perro.hacer_sonido())  # Imprime: Guau
    
    print(gato)          # Imprime: Gato(nombre: Whiskers, edad: 3)
    print(gato.hacer_sonido())  # Imprime: Miau
