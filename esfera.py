

from circulo import Circulo
import math



class Esfera (Circulo):
    def __init__(self, x, y, radio):
        super().__init__(x,y,radio)
    def obtenerVolumen(self):
        return (4*self.radio*math.pi*(self.radio**3))/3
    def obtenerSupercifie(self):
        area = 4*math.pi*(self.radio**2)
        return area
    def aCadea(self):
        cadea = super().toString()+ "\n\t Radio : " + str(self.radio)
        return cadea

esfera = Esfera(2,3,4)
print("esfera",esfera.aCadea(),"superficie : ",esfera.obtenerSupercifie(),"volumen : ",esfera.obtenerVolumen())