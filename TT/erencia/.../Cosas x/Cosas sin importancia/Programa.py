class Persona:
    def __init__(self,nombre,peso):
        self.nombre = nombre
        self.peso = peso
    def caminar(self,*args):
        if len(args)>0:
            self.peso -=args[]