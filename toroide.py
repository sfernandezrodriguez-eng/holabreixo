
from circulo import Circulo
import math





class Toroide (Circulo):
    def __init__(self, x, y, radio,radio2):
        super().__init__(x,y,radio)
        self.radio2 = abs(radio2)
    def obtenerVolumenT(self,radio2,radio):
        r3 = (radio - radio2)/2
        Vt = 2 * math.pi * r3 * super().obtenerArea()
        return Vt
    def obtenerSupercifieT(self,radio2,radio):
        r3 = (radio - radio2) / 2
        area = 4*math.pi**(3/2)*r3*(super().obtenerArea()*0.5)
        return area

    def aCadea(self):
        cadea = super().toString() + "\n\t Radio : " + str(self.radio) + "\n\t Radio 2 : " + str(self.radio2)
        return cadea






cono = Toroide(2,3,4,3,)
print("cono",cono.aCadea(),"\n\t superficie : ",cono.obtenerSupercifieT(3,4),"\n\t volumen : ",cono.obtenerVolumenT(3,4))