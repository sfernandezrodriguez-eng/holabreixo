import math

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def toString(self):
        cadeaPunto= "As coordenadas do punto son: \n\t x= "+ str(self.x) + "\n\t y = "+ str(self.y)
        return cadeaPunto
    def distancia (self, outroPunto):
        return math.sqrt(self.x-outroPunto.x)**2 + (self.y-outroPunto.y)**2
    def __str__(self):
        return self.toString()

