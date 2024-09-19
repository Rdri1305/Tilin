class Persona:
    def __init__(self, nombre='', edad=0, profesion='Desconocida'):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def __str__(self):
        return f'Persona(nombre: {self.nombre}, edad: {self.edad}, profesion: {self.profesion})'

# Ejemplo de uso
if __name__ == "__main__":
    # Caso 1: Inicialización sin argumentos
    persona1 = Persona()
    print(persona1)  # Imprime: Persona(nombre: , edad: 0, profesion: Desconocida)
    
    # Caso 2: Inicialización con solo el nombre
    persona2 = Persona(nombre="Juan")
    print(persona2)  # Imprime: Persona(nombre: Juan, edad: 0, profesion: Desconocida)
    
    # Caso 3: Inicialización con nombre y edad
    persona3 = Persona(nombre="Ana", edad=25)
    print(persona3)  # Imprime: Persona(nombre: Ana, edad: 25, profesion: Desconocida)
    
    # Caso 4: Inicialización con nombre, edad y profesión
    persona4 = Persona(nombre="Carlos", edad=30, profesion="Ingeniero")
    print(persona4)  # Imprime: Persona(nombre: Carlos, edad: 30, profesion: Ingeniero)
