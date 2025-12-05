from circulo import Circulo
import math

class Cilindro (Circulo):
    def __init__(self, x, y, radio,altura):
        super().__init__(x,y,radio)
        self.altura = abs(altura)
    def obtenerVolumen(self,altura):
        return super().obtenerArea()*altura
    def obtenerArea(self,altura):
        area = 2*math.pi*self.radio + (2*math.pi*altura*self.radio)
        return area
    def aCadea(self):
        cadea = super().toString() + "\n\t Radio : " + str(self.radio) + "\n\t Altura : " + str(self.altura)
        return cadea