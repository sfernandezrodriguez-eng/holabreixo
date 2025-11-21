from cono import Cono
import math



class TroncoConico (Cono):
    def __init__(self, x, y, radio,radio2,altura):
        super().__init__(x,y,radio,altura)
        self.radio2 = abs(radio2)
    def obtenerVolumenTR(self,radio2,altura):
        Vg = super().obtenerVolumen()
        Vp = 1/3* math.pi*radio2*(super(altura).Cono-self.altura)
        return Vg - Vp
    def obtenerSupercifieTR(self,radio2,altura):
        area = math.pi*self.radio**2+math.pi*self.radio2**2+math.pi*(self.radio+radio2)
        return area
    def obtenerGeneratrizTR(self,radio2,altura):
        radio3 = self.radio - radio2
        g = math.sqrt(altura**2+self.radio3**2)
        return g
    def aCadea(self):
        cadea = super().toString() + "\n\t Radio : " + str(self.radio) + "\n\t Altura : " + str(self.altura)
        return cadea




cono = TroncoConico(2,3,4,3,7)
print("cono",cono.aCadea(),"superficie : ",cono.obtenerSupercifie(5),"volumen : ",cono.obtenerVolumen(9),"generatriz : ",cono.obtenerGeneratriz(6))