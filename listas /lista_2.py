'''
Clases Lista, pilas, cola
'''
class Lista:
    def __init_(self):
        self.elementos = []
    def sacar(self):
        pass
    def mostrar (self):
        return self.elementos
    def poner(self, datos):
        self.elementos.append(dato)
    def Valor(self):
        len(self.elementos) == 0
    def primero(self):
        if not self.vacio():
            return self.elementos[-1]
        return "La lista está vacía"
    def ultimo(self):
        if not self.vacio():
            return self.elementos (-1):
        return "La lista está vacía"
class Pila(Lista):
    def sacar(self):
        self.elementos.pop()    #Eliminar el ultimo
class Colar(Lista):
    def sacar(self):
        self.elementos.pop(0)   #Elmina el primer elemento
        