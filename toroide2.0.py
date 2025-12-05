from ftplib import parse150

from circulo import Circulo
from objeto_metodo import Punto
import math


class Toroide(Circulo):
    def __init__(self,x,y,r,centro):
        super().__init__(x,y,r)
        self.centroToroX = centro.x
        self.centroToroY = centro.y
    def radioM(self):
        radioMaior = self.distancia(Punto(self.centroToroX, self.centroToroY))
        return radioMaior
    def area(self,radioMaior):

        radioMenor = radioMaior - self.radio
        return 4*math.pi**2*radioMaior*radioMenor
    def volumen(self,radioMaior):
        return 2*math.pi*radioMaior*super().obtenerArea()

    def aCadea(self):
        cadea = super().toString() + "\n\t Radio : " + str(self.radio) + "\n\t Radio 2 : " + str(self.radio2)
        return cadea


p1=Punto(3,6)
cono = Toroide(2,3,4,p1)
print("cono",cono.aCadea(),"\n\t superficie : ",cono.area(3,4),"\n\t volumen : ",cono.volumen(3,4))