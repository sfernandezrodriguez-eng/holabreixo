from circulo import Circulo
import math



class Cono (Circulo):
    def __init__(self, x, y, radio,altura):
        super().__init__(x,y,radio)
        self.altura = abs(altura)
    def obtenerVolumen(self,altura):
        return (super().obtenerArea()*altura)/3
    def obtenerSupercifie(self,altura):
        area = math.pi*self.radio*math.sqrt(altura**2+self.radio**2)+super().obtenerArea()
        return area
    def obtenerGeneratriz(self,altura):
        return math.sqrt(altura**2+self.radio**2)
    def aCadea(self):
        cadea = super().toString() + "\n\t Radio : " + str(self.radio) + "\n\t Altura : " + str(self.altura)
        return cadea